import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QFormLayout, QStackedWidget, QMessageBox
import re
import subprocess  # Import subprocess to run GraphicalUI.py

# Database connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="jatinsql31",
        database="SPYWARE"
    )

# Function to check if username exists
def username_exists(username):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    connection.close()
    return result is not None

# Function to check credentials
def validate_login(username, password):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    connection.close()
    return result is not None

# Function to update password
def update_password(username, new_password):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
    connection.commit()
    connection.close()

# Function to add a new user
def add_user(username, password):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    connection.commit()
    connection.close()

# Main window class
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login / Sign Up")
        self.setFixedSize(500, 600)

        self.layout = QVBoxLayout()
        self.stacked_widget = QStackedWidget(self)

        # Create widgets for login page
        self.login_page = QWidget()
        self.login_layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Enter Username")
        
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login", self)
        self.signup_button = QPushButton("Sign Up", self)
        self.forget_button = QPushButton("Forgot Password?", self)

        self.login_layout.addWidget(QLabel("Username:", self))
        self.login_layout.addWidget(self.username_input)
        self.login_layout.addWidget(QLabel("Password:", self))
        self.login_layout.addWidget(self.password_input)
        self.login_layout.addWidget(self.login_button)
        self.login_layout.addWidget(self.signup_button)
        self.login_layout.addWidget(self.forget_button)
        self.login_page.setLayout(self.login_layout)

        # Create widgets for sign-up page
        self.signup_page = QWidget()
        self.signup_layout = QFormLayout()
        self.signup_username_input = QLineEdit(self)
        self.signup_username_input.setPlaceholderText("Enter Username")

        self.signup_password_input = QLineEdit(self)
        self.signup_password_input.setPlaceholderText("Enter Password")
        self.signup_password_input.setEchoMode(QLineEdit.Password)

        self.signup_button_submit = QPushButton("Submit", self)
        self.back_to_login_button = QPushButton("Back to Login", self)

        self.signup_layout.addRow("Username:", self.signup_username_input)
        self.signup_layout.addRow("Password:", self.signup_password_input)
        self.signup_layout.addRow(self.signup_button_submit)
        self.signup_layout.addRow(self.back_to_login_button)
        self.signup_page.setLayout(self.signup_layout)

        # Add pages to the stacked widget
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.signup_page)

        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)

        # Connect buttons to methods
        self.login_button.clicked.connect(self.handle_login)
        self.signup_button.clicked.connect(self.show_signup_page)
        self.signup_button_submit.clicked.connect(self.handle_signup)
        self.back_to_login_button.clicked.connect(self.show_login_page)
        self.forget_button.clicked.connect(self.show_forgot_password_page)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if validate_login(username, password):
            self.close()  # Close the current window if login is successful
            
            # Run GraphicalUI.py after successful login
            subprocess.run(['python', 'GraphicalUI.py'])  # This will run GraphicalUI.py in a new process
            
        else:
            self.show_message("Invalid username or password.")

    def show_signup_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def handle_signup(self):
        username = self.signup_username_input.text()
        password = self.signup_password_input.text()

        if username_exists(username):
            self.show_message("Username already exists.")
        elif not self.is_valid_password(password):
            self.show_weak_password_message()  # Show weak password message
        else:
            add_user(username, password)
            self.show_message("Account created successfully.")
            self.show_login_page()

    def is_valid_password(self, password):
        return bool(re.match(r'^(?=.*[A-Z])(?=.*[!@#$%^&*])(?=.{8,})', password))

    def show_message(self, message):
        self.message_label = QLabel(message, self)
        self.login_layout.addWidget(self.message_label)

    def show_login_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_forgot_password_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def show_weak_password_message(self):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Weak Password")
        msg.setText("Password is too weak. It must contain at least 8 characters, 1 uppercase letter, and 1 special symbol (@#!%&*).")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

# Main execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
