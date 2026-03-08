from PySide6.QtWidgets import QWidget, QVBoxLayout, QTreeWidget, QTreeWidgetItem, QPushButton, QInputDialog
from modules.pages.page_manager import create_page, get_children

class Sidebar(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()
        
        self.tree = QTreeWidget()
        self.tree.setHeaderLabel("Workspace")
        self.tree.itemClicked.connect(self.on_item_clicked)
        
        self.add_btn = QPushButton("+ New Root Page")
        self.add_btn.clicked.connect(self.add_root_page)
        
        self.layout.addWidget(self.tree)
        self.layout.addWidget(self.add_btn)
        self.setLayout(self.layout)
        self.refresh_tree()

    def refresh_tree(self):
        self.tree.clear()
        roots = get_children(None)
        for page in roots:
            item = QTreeWidgetItem([page[1]]) # title
            item.setData(0, 32, page[0]) # store ID in user role
            self.load_children(item, page[0])
            self.tree.addTopLevelItem(item)

    def load_children(self, parent_item, parent_id):
        children = get_children(parent_id)
        for child in children:
            item = QTreeWidgetItem([child[1]])
            item.setData(0, 32, child[0])
            self.load_children(item, child[0])
            parent_item.addChild(item)

    def add_root_page(self):
        title, ok = QInputDialog.getText(self, "New Page", "Enter page title:")
        if ok and title:
            create_page(title)
            self.refresh_tree()

    def on_item_clicked(self, item, column):
        page_id = item.data(0, 32)
        # This would signal the editor to load page_id
        print(f"Loading page {page_id}")