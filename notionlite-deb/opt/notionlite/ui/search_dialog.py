from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QListWidget
from PySide6.QtCore import Qt
from core.search import search

class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Global Search")
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search notes, tasks, etc...")
        self.search_input.textChanged.connect(self.perform_search)

        self.results_list = QListWidget()
        self.results_list.itemClicked.connect(self.on_item_clicked)

        layout.addWidget(self.search_input)
        layout.addWidget(self.results_list)

        self.search_input.setFocus()

    def perform_search(self, text):
        self.results_list.clear()
        if not text.strip():
            return
            
        # Add wildcard for partial matches
        query = f"*{text}*" if len(text) > 2 else text
        
        try:
            results = search(query)
            for row in results:
                # row[0] should be the title
                self.results_list.addItem(row[0])
        except Exception as e:
            # Table might not exist or other sqlite issue
            self.results_list.addItem(f"Error: {e}")

    def on_item_clicked(self, item):
        # We can emit a signal or handle the selection to load a page.
        # For now, we will just accept the dialog.
        self.accept()
