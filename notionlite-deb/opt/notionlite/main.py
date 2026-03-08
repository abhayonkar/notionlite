import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from core.database import init_db
from core.theme import dark_theme  # Added missing import
from ui.main_window import MainWindow

def main():
    # Initialize the database schema first
    init_db()

    app = QApplication(sys.argv)
    
    # Try to set icon, fallback gracefully if missing
    try:
        app.setWindowIcon(QIcon("assets/icon.png"))
    except:
        pass

    # Apply the dark theme from core.theme
    app.setStyleSheet(dark_theme())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()