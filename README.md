# Student Management Portal (Flask + MySQL)

A simple **Student Management Web Application** built using **Flask, MySQL, and Bootstrap**.  
The system allows students to view their marks and results, while an admin can update student marks.

----------

## Features

### User

-   User signup and login
    
-   View subject marks
    
-   Automatic percentage calculation
    
-   Automatic grade generation
    
-   Update email
    
-   Reset password
    

### Admin

-   Admin login
    
-   Update student marks
    
-   View all student records
    

----------

## Tech Stack

-   **Backend:** Flask (Python)
    
-   **Database:** MySQL
    
-   **Frontend:** HTML, Bootstrap
    
-   **Templating:** Jinja2
    
-   **Authentication:** Session-based login system
    

----------

## Project Structure

```
database-mg/
│
├── app.py
├── templates/
│   ├── admin.html
│   ├── admin_login.html
│   ├── dashboard.html
│   ├── login.html
│   ├── signup.html
│   ├── navbar.html
│   └── update.html
│
├── requirements.txt
└── README.md

```

----------

## Installation

### 1. Clone the repository

```
git clone https://github.com/yourusername/student-management-flask.git
cd student-management-flask

```

### 2. Create virtual environment

```
python -m venv venv

```

### 3. Activate environment

Windows

```
venv\Scripts\activate

```

Mac/Linux

```
source venv/bin/activate

```

### 4. Install dependencies

```
pip install -r requirements.txt

```

### 5. Configure MySQL

Update database credentials inside `app.py`.

```
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'yourpassword'
MYSQL_DB = 'flask_auth'

```

### 6. Run the application

```
python app.py

```

Then open:

```
http://127.0.0.1:5000

```

----------

## How It Works

1.  Users register using the signup page.
    
2.  Admin assigns marks to students through the admin panel.
    
3.  Students can view marks, percentage, and grade on the dashboard.
    

Grade is automatically calculated based on percentage.

----------



## Future Improvements

-   Password hashing for security
    
-   Edit/delete student functionality
    
-   Role-based authentication
    
-   REST API support
    
-   Deploy on cloud (Render / Railway)
    

<!--stackedit_data:
eyJoaXN0b3J5IjpbNjMwNTI3NDY3XX0=
-->