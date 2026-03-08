from PySide6.QtWidgets import (
    QMainWindow,
    QTabWidget,
    QHBoxLayout,
    QWidget
)
from PySide6.QtGui import QShortcut, QKeySequence

from ui.sidebar import Sidebar
from ui.notes_view import NotesView
from ui.tasks_view import TasksView
from ui.kanban_view import KanbanView
from ui.calendar_view import CalendarView
from ui.graph_view import GraphView
from ui.search_dialog import SearchDialog


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("NotionLite")
        self.resize(1200, 800)

        # 1. Create the central widget and main horizontal layout
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 2. Add the Sidebar
        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)

        # 3. Create the Tab Widget for the main content
        self.tabs = QTabWidget()
        self.tabs.addTab(NotesView(), "Notes")
        self.tabs.addTab(TasksView(), "Tasks")
        self.tabs.addTab(KanbanView(), "Kanban")
        self.tabs.addTab(CalendarView(), "Calendar")
        self.tabs.addTab(GraphView(), "Graph")

        # 4. Add tabs to the main layout
        main_layout.addWidget(self.tabs)

        # 5. Set the central widget
        self.setCentralWidget(central_widget)
        
        # Apply some specific styling to distinguish sidebar from content
        self.sidebar.setStyleSheet("""
            QWidget {
                background-color: #252526;
                border-right: 1px solid #333;
            }
        """)

        # Add Search Shortcut
        self.search_shortcut = QShortcut(QKeySequence("Ctrl+P"), self)
        self.search_shortcut.activated.connect(self.show_search_dialog)

    def show_search_dialog(self):
        dialog = SearchDialog(self)
        dialog.exec()

    def load_page(self, page_id):
        """
        Future method to switch the editor view 
        when a page is clicked in the sidebar.
        """
        pass