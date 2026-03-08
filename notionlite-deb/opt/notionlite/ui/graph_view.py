from PySide6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg
from modules.graph.graph_engine import get_graph


class GraphView(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout()

        graph_widget = pg.GraphItem()

        edges = get_graph()

        pos = []
        adj = []

        for s,t in edges:
            pos.append((s,t))
            adj.append((s,t))

        graph_widget.setData(
            pos=pos,
            adj=adj
        )

        view = pg.GraphicsLayoutWidget()
        plot = view.addPlot()

        plot.addItem(graph_widget)

        layout.addWidget(view)

        self.setLayout(layout)