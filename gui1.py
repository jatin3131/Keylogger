import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QLabel, QFrame, QTableWidget, QTableWidgetItem
)
from PyQt5.QtGui import QFont, QPalette, QColor, QIcon
from PyQt5.QtCore import Qt

class DashboardUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Dashboard UI")
        self.resize(1200, 800)
        self.setStyleSheet("background-color: #0f0f1b; color: white;")

        # Main Container Layout
        main_layout = QHBoxLayout()
        
        # Sidebar
        sidebar = self.create_sidebar()
        main_layout.addWidget(sidebar)

        # Main Content
        main_content = self.create_main_content()
        main_layout.addWidget(main_content, stretch=3)

        # Central Widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def create_sidebar(self):
        """Create sidebar menu."""
        sidebar = QFrame()
        sidebar.setFixedWidth(200)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: #1a1a2e;
                border-right: 2px solid #32325d;
            }
            QLabel {
                color: white;
                font-size: 14px;
            }
        """)
        sidebar_layout = QVBoxLayout()

        # App Title
        title = QLabel("VISION UI PRO")
        title.setFont(QFont("Arial", 12, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(title)

        # Navigation Labels
        nav_labels = ["Dashboard", "Pages", "Applications", "Ecommerce", "Authentication"]
        for label in nav_labels:
            lbl = QLabel(f"📄 {label}")
            lbl.setAlignment(Qt.AlignLeft)
            lbl.setStyleSheet("padding: 8px; font-size: 14px;")
            sidebar_layout.addWidget(lbl)

        sidebar_layout.addStretch()
        sidebar.setLayout(sidebar_layout)
        return sidebar

    def create_main_content(self):
        """Create main content area."""
        main_frame = QFrame()
        layout = QVBoxLayout()

        # General Statistics Section
        stats_layout = QHBoxLayout()
        stats = [
            ("Today's Money", "$53,000", "+55%"),
            ("New Clients", "+3,020", "-14%"),
            ("Today's Users", "2,300", "+5%"),
            ("Total Sales", "173,000", "+8%")
        ]
        for title, value, change in stats:
            stat_card = self.create_stat_card(title, value, change)
            stats_layout.addWidget(stat_card)

        layout.addLayout(stats_layout)

        # The Sales by Country Table is removed
        # table_label = QLabel("Sales by Country")
        # table_label.setFont(QFont("Arial", 14, QFont.Bold))
        # layout.addWidget(table_label)

        # table = self.create_table()
        # layout.addWidget(table)

        main_frame.setLayout(layout)
        return main_frame

    def create_stat_card(self, title, value, change):
        """Create a single statistics card."""
        card = QFrame()
        card.setFixedHeight(120)
        card.setStyleSheet("""
            QFrame {
                background-color: #212146;
                border-radius: 10px;
                padding: 10px;
            }
            QLabel {
                color: white;
            }
        """)

        vbox = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setFont(QFont("Arial", 12))
        value_label = QLabel(value)
        value_label.setFont(QFont("Arial", 18, QFont.Bold))
        change_label = QLabel(change)
        change_label.setStyleSheet("color: #00FF00;" if "+" in change else "color: #FF5733;")
        vbox.addWidget(title_label)
        vbox.addWidget(value_label)
        vbox.addWidget(change_label)
        card.setLayout(vbox)
        return card

    # The table creation function is now removed, as we no longer need it.
    # def create_table(self):
    #     """Create the country sales table."""
    #     table = QTableWidget()
    #     table.setColumnCount(4)
    #     table.setRowCount(4)
    #     table.setHorizontalHeaderLabels(["Country", "Sales", "Value", "Bounce"])
    #     table.horizontalHeader().setStyleSheet("""
    #         QHeaderView::section {
    #             background-color: #32325d;
    #             color: white;
    #             font-weight: bold;
    #             padding: 5px;
    #         }
    #     """)
    #     table.verticalHeader().setVisible(False)
    #     table.setStyleSheet("QTableWidget { background-color: #1f1f3d; color: white; }")

    #     # Table Data
    #     data = [
    #         ("United States", "2500", "$214,000", "40.22%"),
    #         ("Germany", "3900", "$446,700", "19.22%"),
    #         ("Great Britain", "1300", "$121,900", "39.22%"),
    #         ("Brasil", "920", "$52,100", "29.9%")
    #     ]

    #     for row, (country, sales, value, bounce) in enumerate(data):
    #         table.setItem(row, 0, QTableWidgetItem(country))
    #         table.setItem(row, 1, QTableWidgetItem(sales))
    #         table.setItem(row, 2, QTableWidgetItem(value))
    #         table.setItem(row, 3, QTableWidgetItem(bounce))

    #     table.resizeColumnsToContents()
    #     table.setFixedHeight(300)
    #     return table


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = DashboardUI()
    window.show()
    sys.exit(app.exec_())
