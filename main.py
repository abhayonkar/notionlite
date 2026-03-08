import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from core.database import init_db
from ui.main_window import MainWindow


def main():

    init_db()

    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon("assets/icon.png"))
    app.setStyleSheet(dark_theme())

    window = MainWindow()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()