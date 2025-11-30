import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class SendingAnimation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A → B Animation")
        self.setFixedSize(600, 200)
        self.setStyleSheet("background-color: #1a1a2e;")
        self.position = 50  # Initial position of the moving object
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_position)
        self.timer.start(20)  # Update every 20ms for smooth animation

    def update_position(self):
        """Update the position of the moving object."""
        self.position += 5  # Move to the right
        if self.position > self.width() - 100:  # Reset position when reaching near 'B'
            self.position = 50
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        """Custom paint for the A → B animation."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw 'A'
        painter.setPen(Qt.white)
        painter.setFont(self.font())
        painter.drawText(20, self.height() // 2, "A")

        # Draw 'B'
        painter.drawText(self.width() - 40, self.height() // 2, "B")

        # Draw the moving object (circle)
        painter.setBrush(QBrush(QColor("#4caf50")))  # Green circle
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.position, self.height() // 2 - 10, 20, 20)  # Moving circle

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Show A → B Animation
    animation = SendingAnimation()
    animation.show()

    sys.exit(app.exec_())
