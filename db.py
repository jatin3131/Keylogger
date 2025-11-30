from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLineEdit, QLabel, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
import sys

# Existing DashboardUI class remains unchanged
# Add this LoginDialog class

class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)

        # Center the login dialog on the screen
        self.move(QApplication.primaryScreen().geometry().center() - self.rect().center())

        # Create layout
        layout = QVBoxLayout()

        # Username label and input
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter your username")
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        # Password label and input
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter your password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        # Login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.validate_login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def validate_login(self):
        """Validate username and password"""
        username = self.username_input.text()
        password = self.password_input.text()

        # Replace with your actual authentication logic
        if username == "admin" and password == "password":
            QMessageBox.information(self, "Login Successful", "Welcome to the dashboard!")
            self.accept()  # Close the dialog and allow the main window to open
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password!")

# Modify the main function
def main():
    app = QApplication(sys.argv)

    # Show login dialog first
    login_dialog = LoginDialog()
    if login_dialog.exec_() == QDialog.Accepted:  # If login is successful
        window = DashboardUI()
        window.show()
        sys.exit(app.exec_())
    else:
        sys.exit(0)  # Exit if login fails or is canceled

if __name__ == "__main__":
    main()
