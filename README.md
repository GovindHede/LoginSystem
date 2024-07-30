# Login System

This is a Django-based login system project that includes functionalities for user signup, login, welcome page, and password reset (forgot password).

## Features

- **User Signup**: Users can create an account by providing a username, email, and password.
- **User Login**: Registered users can log in using their username and password.
- **Welcome Page**: Authenticated users are greeted with a welcome message.
- **Forgot Password**: Users can reset their password if they forget it.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name



#Usage
###Signup
Go to /signup to create a new account.
Provide a username, email, password, and confirm the password.
On successful signup, you will be redirected to the login page.
###Login
Go to /login to log into your account.
Provide your username and password.
On successful login, you will be redirected to the welcome page.
###Welcome Page
After logging in, you will be redirected to the /welcome page.
The welcome page displays a greeting message with your username.
###Forgot Password
Go to /forgot if you need to reset your password.
Follow the instructions to reset your password.

#project structure

login_system/
├── login/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── login_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── signup.html
│   ├── login.html
│   ├── welcome.html
│   └── forgot.html
├── manage.py
└── requirements.txt


Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any improvements.
