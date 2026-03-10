from flask import Flask, render_template, request, redirect, session,flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "secret"

# MySQL config
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root1234'
app.config['MYSQL_DB'] = 'flask_auth'

mysql = MySQL(app)

# ---------- Signup ----------
@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("""
        INSERT INTO users(username,email,password,physics,chemistry,mathematics,english)
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """,(username,email,password,None,None,None,None))

        mysql.connection.commit()
        cur.close()

        return redirect('/login')

    return render_template('signup.html')


# ---------- Login ----------
@app.route('/', methods=['GET','POST'])
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s",
                    (username,password))
        user = cur.fetchone()
        cur.close()

        if user:
            session['user'] = username
            return redirect('/dashboard')

    return render_template('login.html')


# ---------- Dashboard ----------
@app.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    cur = mysql.connection.cursor()

    cur.execute("""
    SELECT username,email,physics,chemistry,mathematics,english
    FROM users WHERE username=%s
    """,(session['user'],))

    user = cur.fetchone()
    cur.close()

    physics, chemistry, math, english = user[2], user[3], user[4], user[5]

    percentage = None
    grade = None

    if None not in (physics, chemistry, math, english):

        percentage = (physics + chemistry + math + english) / 4

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

    return render_template(
        'dashboard.html',
        user=user,
        percentage=percentage,
        grade=grade
    )


# ---------- Update Profile ----------
@app.route('/update', methods=['GET','POST'])
def update():

    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE users SET email=%s WHERE username=%s",
                    (email,session['user']))
        mysql.connection.commit()
        cur.close()

        return redirect('/dashboard')

    return render_template('update.html')


# ---------- Reset Password ----------
@app.route('/reset', methods=['POST'])
def reset():

    if 'user' not in session:
        return redirect('/login')

    newpass = request.form.get('password')

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE users SET password=%s WHERE username=%s",
        (newpass, session['user'])
    )
    mysql.connection.commit()
    cur.close()

    flash("Password updated successfully!", "success")
    return redirect('/dashboard')


# ---------- Admin Login ----------
@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s",
                    (username,password))
        admin = cur.fetchone()

        if admin:
            session['admin'] = username
            return redirect('/admin_panel')

    return render_template('admin_login.html')


# ---------- Admin Panel ----------
@app.route('/admin_panel', methods=['GET','POST'])
def admin_panel():

    if 'admin' not in session:
        return redirect('/admin')

    cur = mysql.connection.cursor()

    if request.method == 'POST':
        username = request.form['username']
        physics = request.form['physics']
        chemistry = request.form['chemistry']
        mathematics = request.form['mathematics']
        english = request.form['english']

        cur.execute("""
        UPDATE users
        SET physics=%s, chemistry=%s, mathematics=%s, english=%s
        WHERE username=%s
        """,(physics,chemistry,mathematics,english,username))

        mysql.connection.commit()

    cur.execute("SELECT username,physics,chemistry,mathematics,english FROM users")
    users = cur.fetchall()

    return render_template('admin.html', users=users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)