from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QPushButton
)

from modules.notes.notes_manager import add_note


class NotesView(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        self.editor = QTextEdit()

        save = QPushButton("Save Note")

        save.clicked.connect(self.save_note)

        layout.addWidget(self.editor)
        layout.addWidget(save)

        self.setLayout(layout)

    def save_note(self):

        text = self.editor.toPlainText()

        add_note("Quick Note",text)

        self.editor.clear()