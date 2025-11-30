import sys
import math
from PyQt5.QtCore import Qt, QTimer, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor, QConicalGradient
from PyQt5.QtWidgets import QApplication, QWidget


class RadarWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radar Simulation")
        self.setFixedSize(400, 400)
        self.setStyleSheet("background-color: #1a1a2e;")
        self.angle = 0  # Initial angle of the scanning beam
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_angle)
        self.timer.start(20)  # Update every 20ms for smooth animation

    def update_angle(self):
        """Update the angle of the scanning beam."""
        self.angle = (self.angle + 2) % 360  # Increment the angle
        self.update()  # Trigger a repaint

    def paintEvent(self, event):
        """Custom paint for the radar."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the radar circle (world map placeholder)
        center = self.rect().center()
        radius = min(self.width(), self.height()) // 2 - 20
        painter.setPen(QPen(Qt.white, 2))
        painter.drawEllipse(center, radius, radius)

        # Draw the scanning beam
        gradient = QConicalGradient(center, self.angle)
        gradient.setColorAt(0, QColor(0, 255, 0, 150))  # Green fading effect
        gradient.setColorAt(0.5, QColor(0, 255, 0, 50))
        gradient.setColorAt(1, QColor(0, 0, 0, 0))
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawPie(
            center.x() - radius,
            center.y() - radius,
            radius * 2,
            radius * 2,
            (self.angle - 45) * 16,
            90 * 16,
        )

        # Draw gridlines
        painter.setPen(QPen(QColor(80, 255, 80), 1))
        for i in range(4):
            angle = math.radians(90 * i)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            painter.drawLine(center, center + QPointF(x, y))

        # Draw concentric circles
        for r in range(50, radius, 50):
            painter.drawEllipse(center, r, r)

        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and display the radar widget
    radar = RadarWidget()
    radar.show()

    sys.exit(app.exec_())
