import pyqtgraph as pg
from PySide6 import QtWidgets,QtCore


class plotBox(QtWidgets.QMainWindow):
    def __init__(self,Title):
        super().__init__()
        
        self.graph = pg.PlotWidget()
        self.graph.setBackground("w")
        self.graph.setTitle(Title, color="b", size="20pt")
        styles = {"color": "red", "font-size": "18px"}
        self.graph.setLabel("bottom", "Time", **styles)
        self.graph.setLabel("left","Value", **styles)
        self.graph.addLegend()
        self.graph.showGrid(x=True, y=True)
        self.graph.setYRange(0, 37)
        self.setCentralWidget(self.graph)
   