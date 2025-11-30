import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QDialog, QTextEdit, QProgressBar
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer


class DashboardUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SPYWARE")
        self.setGeometry(100, 100, 800, 600)  # Optional, but you can still set initial position/size
        self.showMaximized()

        # Main container widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Main layout
        main_layout = QHBoxLayout(main_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Sidebar
        sidebar = QVBoxLayout()
        sidebar.setSpacing(15)  # Add spacing between sidebar buttons
        sidebar.setContentsMargins(0, 0, 0, 0)

        sidebar_label = QLabel("SPYWARE")
        sidebar_label.setFont(QFont("Arial", 16, QFont.Bold))
        sidebar_label.setStyleSheet("color: white;")
        sidebar_label.setAlignment(Qt.AlignCenter)
        sidebar.addWidget(sidebar_label)

        # Create buttons for sidebar (Button 5 to Button 7)
        for i in range(3):  # Only create 3 buttons now (no Button 4)
            if i == 0:
                btn = QPushButton("Captured Logs")
                btn.clicked.connect(self.run_read_logs_script)
            elif i == 1:
                btn = QPushButton("Notes")
                btn.clicked.connect(self.run_notes_script)
            elif i == 2:
                btn = QPushButton("About Us")
                btn.clicked.connect(self.show_about_us)  # Connect the button to the "About Us" function

            btn.setStyleSheet(
                "background-color: #2c2c54; color: white; padding: 10px; font-size: 14px; border: none;"
            )
            sidebar.addWidget(btn)

        # Add sidebar to the layout
        sidebar_container = QWidget()
        sidebar_container.setLayout(sidebar)
        sidebar_container.setStyleSheet(
            "background-color: #1e1e2f; padding: 0; border-right: 2px solid #444;"
        )  # Add line on the right side
        sidebar_container.setFixedWidth(200)
        main_layout.addWidget(sidebar_container, 2)

        # Main content button
        content_layout = QVBoxLayout()
        content_layout.setSpacing(0)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # Top section (Placeholder for Buttons)
        image1_label = QLabel()
        image1_pixmap = QPixmap("SPYWARE")  # Replace with your actual image file path
        image1_label.setPixmap(image1_pixmap)
        image1_label.setScaledContents(True)
        image1_label.setStyleSheet("border-bottom: 2px solid #444; background-color: #1e1e2f;")
        content_layout.addWidget(image1_label, 5)

        # Bottom section with image2_label
        self.image2_label = QLabel()
        image2_pixmap = QPixmap("bottom3")  # Replace with your actual image file path
        self.image2_label.setPixmap(image2_pixmap)
        self.image2_label.setScaledContents(True)
        self.image2_label.setFixedHeight(200)  # Set height to 200
        self.image2_label.setStyleSheet("background-color: gray; border-top: 2px solid #444;")

        # Overlay QLabel for dynamic text
        self.dynamic_text_label = QLabel(self.image2_label)
        self.dynamic_text_label.setStyleSheet("color: white; font-size: 14px; background: transparent;")
        self.dynamic_text_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.dynamic_text_label.setGeometry(10, 10, self.image2_label.width() - 20, self.image2_label.height() - 20)

        # Add bottom section to content layout
        content_layout.addWidget(self.image2_label, 2)

        # Add content to the layout
        main_layout.addLayout(content_layout, 4)

        # Buttons on the top image
        self.start_server_button = self.create_button("Start Server", image1_label, -150, -70, self.start_server)
        self.stop_server_button = self.create_button("Stop Server", image1_label, -150, 70, self.stop_server)

        # Changed "New Button" to "Clear Logs"
        self.clear_logs_button = self.create_button("Clear Logs", image1_label, 150, -70, self.clear_logs)
        self.save_logs_button = self.create_button("Save Logs", image1_label, 150, 70, self.save_logs)

        # Circle below the Stop Server button
        self.server_status_circle = QLabel(self)
        self.server_status_circle.setFixedSize(50, 50)  # Make it a smaller circle for better visibility
        self.server_status_circle.setStyleSheet("background-color: gray; border-radius: 25px;")  # Gray circle

        # Position the circle just below the Stop Server button
        stop_button_rect = self.stop_server_button.geometry()
        self.server_status_circle.move(
            stop_button_rect.center().x() - self.server_status_circle.width() // 2,
            stop_button_rect.bottom() + 30  # Adjust the vertical positioning as needed
        )

        # Timer to update text dynamically
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_dynamic_text)
        self.timer.start(1000)  # Update every 1 second

        self.server_process = None  # To store the server process

    def create_button(self, text, parent, offset_x, offset_y, function=None):
        """Helper function to create styled buttons"""
        button = QPushButton(text, parent)
        button.setStyleSheet(""" 
            QPushButton {
                background-color: #2c2c54; color: white; padding: 20px; font-size: 16px; border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #00FFFF; color: black;
                transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
            }
        """)
        button.setFixedSize(120, 120)
        button.move(
            (parent.width() - button.width()) // 2 + offset_x,
            (parent.height() - button.height()) // 2 + offset_y,
        )
        if function:
            button.clicked.connect(function)
        return button

    def update_dynamic_text(self):
        """Read the key_logs.txt file and update the dynamic text label with the last few lines"""
        try:
            with open("key_logs.txt", "r") as file:
                lines = file.readlines()[-10:]  # Read the last 10 lines
                logs = "".join(lines)
                self.dynamic_text_label.setText(logs)
        except FileNotFoundError:
            self.dynamic_text_label.setText("key_logs.txt not found!")
        except Exception as e:
            self.dynamic_text_label.setText(f"Error: {e}")

    def run_notes_script(self):
        """Run the Notes.py script when the 'Notes' button is clicked"""
        try:
            subprocess.Popen(["python", "Notes.py"])  # Make sure 'Notes.py' is in the same directory
            print("Notes script started")
        except Exception as e:
            print(f"Error starting Notes script: {e}")

    def start_server(self):
        """Start the server when the button is clicked"""
        try:
            self.server_process = subprocess.Popen(["python", "server.py"])  # Make sure 'server.py' is in the same directory
            print("Server started")
            self.start_server_button.setStyleSheet("""
            QPushButton {
                background-color: #39FF14;  /* Neon green */
                color: black;
                padding: 20px;
                font-size: 16px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #32CD32;  /* Slightly darker neon green */
                color: black;
                transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
            }
        """)

            self.server_status_circle.setStyleSheet("background-color: lightgreen; border-radius: 10px;")  # Turn circle green
        except Exception as e:
            print(f"Error starting server: {e}")

    def stop_server(self):
        """Stop the server when the button is clicked"""
        if self.server_process:
            try:
                self.server_process.terminate()
                self.server_process = None
                print("Server stopped")
                self.start_server_button.setStyleSheet("""
                QPushButton {
                    background-color: #2c2c54;
                    color: white;
                    padding: 20px;
                    font-size: 16px;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #00FFFF;
                    color: black;
                    transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
                }
            """)
                self.server_status_circle.setStyleSheet("background-color: gray; border-radius: 10px;")  # Turn circle gray
            except Exception as e:
                print(f"Error stopping server: {e}")
        else:
            print("No server process running")

    def run_read_logs_script(self):
        """Run the ReadLogs.py script when the 'Captured Logs' button is clicked"""
        try:
            subprocess.Popen(["python", "ReadLog.py"])  # Make sure 'ReadLogs.py' is in the same directory
            print("ReadLogs script started")
        except Exception as e:
            print(f"Error starting ReadLogs script: {e}")

    def clear_logs(self):
        """Clear all content in the key_logs.txt file"""
        try:
            with open("key_logs.txt", "w") as file:
                file.truncate(0)  # Clear the content of the file
            print("Logs cleared successfully")
        except Exception as e:
            print(f"Error clearing logs: {e}")

    def show_about_us(self):
        """Display 'About Us' content from about.txt"""
        try:
            # Open the about.txt file and read its content
            with open("about.txt", "r") as file:
                about_content = file.read()

            # Create a new dialog to display the About Us content
            about_dialog = QDialog(self)
            about_dialog.setWindowTitle("About Us")
            about_dialog.setFixedSize(400, 300)

            # Set layout for the dialog
            layout = QVBoxLayout(about_dialog)

            # Text area to display content
            about_text = QTextEdit(about_dialog)
            about_text.setText(about_content)
            about_text.setReadOnly(True)  # Make the text read-only so users can't edit it
            layout.addWidget(about_text)

            # Center the dialog on the screen
            about_dialog.move(QApplication.primaryScreen().geometry().center() - about_dialog.rect().center())

            about_dialog.exec_()  # Show the dialog

        except FileNotFoundError:
            print("about.txt not found!")
            self.dynamic_text_label.setText("Error: 'about.txt' file not found.")
        except Exception as e:
            print(f"Error opening about.txt: {e}")
            self.dynamic_text_label.setText(f"Error: {e}")

    def save_logs(self):
        """Handle the log saving process"""
        # Start the loading animation
        self.show_loading_animation()
        subprocess.run(["python", "sentData.py"])

        # Simulate saving process (this should be your actual saving logic)
        QTimer.singleShot(2000, self.complete_log_saving)  # Simulate a 3-second delay

    def show_loading_animation(self):
        """Display loading dialog with neon blue progress bar"""
        self.loading_dialog = QDialog(self)
        self.loading_dialog.setWindowTitle("Saving Logs")
        self.loading_dialog.setFixedSize(300, 200)

        # Center the loading dialog
        self.loading_dialog.move(QApplication.primaryScreen().geometry().center() - self.loading_dialog.rect().center())

        # Set background image
        loading_bg = QPixmap("load.jpg")  # Make sure this image exists
        background_label = QLabel(self.loading_dialog)
        background_label.setPixmap(loading_bg)
        background_label.setScaledContents(True)
        background_label.setGeometry(0, 0, 300, 200)

        # Set up progress bar (neon blue color)
        self.progress_bar = QProgressBar(self.loading_dialog)
        self.progress_bar.setGeometry(50, 120, 200, 20)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 2px solid #2c2c54;
                border-radius: 5px;
                text-align: center;
                background-color: #1e1e2f;
            }
            QProgressBar::chunk {
                background-color: #00FFFF;
            }
        """)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)

        # Add label for loading message
        self.loading_label = QLabel("Inserting logs in database...", self.loading_dialog)
        self.loading_label.setGeometry(50, 50, 200, 40)
        self.loading_label.setStyleSheet("color: white; font-size: 16px;")
        self.loading_label.setAlignment(Qt.AlignCenter)

        # Show loading dialog
        self.loading_dialog.show()

        # Set up a timer to simulate progress
        self.progress_timer = QTimer(self)
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_timer.start(50)  # Update every 50ms

        self.progress_value = 0

    def update_progress(self):
        """Update progress bar during loading"""
        if self.progress_value < 100:
            self.progress_value += 1
            self.progress_bar.setValue(self.progress_value)
        else:
            self.progress_timer.stop()
            self.complete_log_saving()

    def complete_log_saving(self):
        """Handle the completion of saving logs"""
        # Close the loading dialog
        self.loading_dialog.accept()

        # Show confirmation message
        self.confirmation_dialog = QDialog(self)
        self.confirmation_dialog.setWindowTitle("Logs Saved")
        self.confirmation_dialog.setFixedSize(200, 100)
        self.confirmation_dialog.move(QApplication.primaryScreen().geometry().center() - self.confirmation_dialog.rect().center())

        confirmation_label = QLabel("Logs have been saved successfully.", self.confirmation_dialog)
        confirmation_label.setAlignment(Qt.AlignCenter)
        confirmation_label.setStyleSheet("color: green; font-size: 14px;")

        self.confirmation_dialog.show()
        QTimer.singleShot(2000, self.confirmation_dialog.accept)  # Close dialog after 2 seconds

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardUI()
    window.show()
    sys.exit(app.exec_())
