
from PySide6.QtWidgets import QWidget, QVBoxLayout, QCalendarWidget, QLabel

class CalendarView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        
        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        
        info_label = QLabel("Select a date to view scheduled tasks or notes.")
        info_label.setStyleSheet("color: #888; padding: 10px;")
        
        layout.addWidget(self.calendar)
        layout.addWidget(info_label)
        self.setLayout(layout)