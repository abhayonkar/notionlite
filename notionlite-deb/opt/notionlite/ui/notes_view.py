from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QSplitter,
    QPlainTextEdit,
    QTextBrowser,
    QPushButton
)
from PySide6.QtCore import Qt

from modules.notes.notes_manager import add_note


class NotesView(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        
        self.editor = QPlainTextEdit()
        self.editor.setPlaceholderText("Write markdown here...")
        self.editor.textChanged.connect(self.update_preview)

        self.preview = QTextBrowser()
        self.preview.setOpenExternalLinks(True)

        self.splitter.addWidget(self.editor)
        self.splitter.addWidget(self.preview)

        save = QPushButton("Save Note")
        save.clicked.connect(self.save_note)

        layout.addWidget(self.splitter)
        layout.addWidget(save)

        self.setLayout(layout)

    def update_preview(self):
        text = self.editor.toPlainText()
        # Fallback using natively supported setMarkdown
        self.preview.setMarkdown(text)

    def save_note(self):
        text = self.editor.toPlainText()
        if text.strip():
            add_note("Quick Note", text)
            self.editor.clear()