import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class DashboardUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Modern Dashboard UI")
        self.setGeometry(100, 100, 800, 600)

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

        for i in range(4):
            btn = QPushButton(f"Button {i + 4}")
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
        sidebar_container.setFixedWidth(200)  # Increase the width of the sidebar further
        main_layout.addWidget(sidebar_container, 2)

        # Main content
        content_layout = QVBoxLayout()
        content_layout.setSpacing(0)
        content_layout.setContentsMargins(0, 0, 0, 0)

        # Image 1 with actual image
        image1_label = QLabel()
        image1_pixmap = QPixmap("SPYWARE")  # Replace with your actual image file path
        image1_label.setPixmap(image1_pixmap)
        image1_label.setScaledContents(True)
        image1_label.setStyleSheet("border-bottom: 2px solid #444; background-color: #1e1e2f;")  # Add line at the bottom and match sidebar background color

        # Start server button
        self.start_server_button = QPushButton("Start Server")
        self.start_server_button.clicked.connect(self.start_server)
        self.start_server_button.setStyleSheet(
            "background-color: #2c2c54; color: white; padding: 20px; font-size: 16px; border-radius: 10px;"
        )
        self.start_server_button.setFixedSize(120, 120)
        self.start_server_button.setParent(image1_label)
        self.start_server_button.move(
            (image1_label.width() - self.start_server_button.width()) // 2 - 150,
            (image1_label.height() - self.start_server_button.height()) // 2,
        )
        self.start_server_button.show()

        # Hover animation (neon blue on hover)
        self.start_server_button.setStyleSheet("""
            QPushButton {
                background-color: #2c2c54; color: white; padding: 20px; font-size: 16px; border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #00FFFF; color: black;
                transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
            }
        """)

        # New button
        new_button = QPushButton("New Button")
        new_button.setStyleSheet(
            "background-color: #2c2c54; color: white; padding: 20px; font-size: 16px; border-radius: 10px;"
        )
        new_button.setFixedSize(120, 120)
        new_button.setParent(image1_label)
        new_button.move(
            (image1_label.width() - new_button.width()) // 2 + 150,
            (image1_label.height() - new_button.height()) // 2,
        )
        new_button.show()

        # Hover animation (neon blue on hover)
        new_button.setStyleSheet("""
            QPushButton {
                background-color: #2c2c54; color: white; padding: 20px; font-size: 16px; border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #00FFFF; color: black;
                transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
            }
        """)

        # Stop server button
        self.stop_server_button = QPushButton("Stop Server")
        self.stop_server_button.setStyleSheet(
            "background-color: #2c2c54; color: white; padding: 20px; font-size: 16px; border-radius: 10px;"
        )
        self.stop_server_button.setFixedSize(120, 120)
        self.stop_server_button.setParent(image1_label)
        self.stop_server_button.move(
            (image1_label.width() - self.stop_server_button.width()) // 2 - 150,
            (image1_label.height() - self.stop_server_button.height()) // 2 + 150,
        )
        self.stop_server_button.show()

        # Hover animation (neon blue on hover)
        self.stop_server_button.setStyleSheet("""
            QPushButton {
                background-color: #2c2c54; color: white; padding: 20px; font-size: 16px; border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #00FFFF; color: black;
                transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
            }
        """)

        # Save logs button
        save_logs_button = QPushButton("Save Logs")
        save_logs_button.setStyleSheet(
            "background-color: #2c2c54; color: white; padding: 20px; font-size: 16px; border-radius: 10px;"
        )
        save_logs_button.setFixedSize(120, 120)
        save_logs_button.setParent(image1_label)
        save_logs_button.move(
            (image1_label.width() - save_logs_button.width()) // 2 + 150,
            (image1_label.height() - save_logs_button.height()) // 2 + 150,
        )
        save_logs_button.show()

        # Hover animation (neon blue on hover)
        save_logs_button.setStyleSheet("""
            QPushButton {
                background-color: #2c2c54; color: white; padding: 20px; font-size: 16px; border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #00FFFF; color: black;
                transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out;
            }
        """)

        content_layout.addWidget(image1_label, 5)

        # Image 2 with actual image
        image2_label = QLabel()
        image2_pixmap = QPixmap("bottom3")  # Replace with your actual image file path
        image2_label.setPixmap(image2_pixmap)
        image2_label.setScaledContents(True)
        image2_label.setFixedHeight(200)  # Set height to 200
        image2_label.setStyleSheet("background-color: gray; border-top: 2px solid #444;")  # Add line at the top
        content_layout.addWidget(image2_label, 2)

        # Add content to the layout
        main_layout.addLayout(content_layout, 4)

        self.server_process = None  # To store the server process

    def start_server(self):
        """Start the server when the button is clicked"""
        try:
            self.server_process = subprocess.Popen(["python", "server.py"])  # Make sure 'server.py' is in the same directory
            print("Server started")
        except Exception as e:
            print(f"Error starting server: {e}")

    def stop_server(self):
        """Stop the server when the button is clicked"""
        if self.server_process:
            try:
                self.server_process.terminate()
                self.server_process = None
                print("Server stopped")
            except Exception as e:
                print(f"Error stopping server: {e}")
        else:
            print("No server process running")

def main():
    app = QApplication(sys.argv)
    window = DashboardUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
