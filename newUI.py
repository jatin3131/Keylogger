from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFrame, QTextEdit
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class DashboardUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Neon Server Dashboard")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: #121212;")

        # Main Layout
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        # Sidebar
        sidebar_container = QWidget()
        sidebar_container.setStyleSheet("""
            background-color: #1e1e2f;
            padding: 0;
            border-right: 2px solid #00ffff;
        """)
        sidebar_layout = QVBoxLayout()
        sidebar_container.setLayout(sidebar_layout)

        # Sidebar Buttons
        btn_names = ["Dashboard", "Logs", "Settings"]
        for name in btn_names:
            btn = QPushButton(name)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #2c2c54;
                    color: white;
                    padding: 10px;
                    font-size: 14px;
                    border: none;
                    border-radius: 5px;
                    margin: 5px;
                    box-shadow: 0 0 10px #00ffff;
                }
                QPushButton:hover {
                    background-color: #00ffff;
                    color: black;
                }
            """)
            sidebar_layout.addWidget(btn)

        sidebar_layout.addStretch()
        main_layout.addWidget(sidebar_container, 1)

        # Content Layout
        content_container = QWidget()
        content_layout = QVBoxLayout()
        content_container.setLayout(content_layout)
        main_layout.addWidget(content_container, 4)

        # Image 1
        image1_label = QLabel()
        image1_label.setPixmap(QPixmap("image1.png").scaled(400, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        image1_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(image1_label)

        # Neon Divider Line
        neon_line = QFrame()
        neon_line.setFrameShape(QFrame.HLine)
        neon_line.setStyleSheet("color: #00ffff; background-color: #00ffff; height: 2px;")
        neon_line.setFixedHeight(2)
        content_layout.addWidget(neon_line)

        # Image 2
        image2_label = QLabel()
        image2_label.setPixmap(QPixmap("image2.png").scaled(400, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        image2_label.setAlignment(Qt.AlignCenter)
        content_layout.addWidget(image2_label)

        # Server Info Row
        server_row = QHBoxLayout()
        server_label = QLabel("Server Status:")
        server_label.setStyleSheet("color: white; font-size: 16px;")
        server_row.addWidget(server_label)

        self.server_status_circle = QLabel()
        self.server_status_circle.setFixedSize(25, 25)
        self.server_status_circle.setStyleSheet("""
            background-color: lightgreen;
            border-radius: 25px;
            border: 2px solid #00ffcc;
            box-shadow: 0 0 20px #00ffcc;
        """)
        server_row.addWidget(self.server_status_circle)
        server_row.addStretch()
        content_layout.addLayout(server_row)

        # Log Viewer
        self.log_text = QTextEdit()
        self.log_text.setStyleSheet("""
            background-color: #1f1f1f;
            color: #00ffff;
            font-family: Consolas;
            font-size: 13px;
            border: 2px solid #00ffff;
            border-radius: 8px;
        """)
        self.log_text.setPlaceholderText("Logs will appear here...")
        self.log_text.setReadOnly(True)
        content_layout.addWidget(self.log_text)

        # Example log content (optional)
        self.log_text.append("⚡ Server started on 127.0.0.1:5000")
        self.log_text.append("✅ Listening for incoming connections...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DashboardUI()
    window.show()
    sys.exit(app.exec_())
