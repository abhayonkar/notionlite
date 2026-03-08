from PySide6.QtWidgets import (
    QMainWindow,
    QTabWidget
)

from ui.notes_view import NotesView
from ui.tasks_view import TasksView
from ui.kanban_view import KanbanView
from ui.calendar_view import CalendarView


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("NotionLite")
        self.resize(1000,700)

        tabs = QTabWidget()

        tabs.addTab(NotesView(),"Notes")
        tabs.addTab(TasksView(),"Tasks")
        tabs.addTab(KanbanView(),"Kanban")
        tabs.addTab(CalendarView(),"Calendar")

        self.setCentralWidget(tabs)