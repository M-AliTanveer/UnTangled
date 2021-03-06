import re
import networkx as nx
import matplotlib.pyplot as plt
from GraphClass import *
from UICode import *
import sys

obj = Graph()
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
ui.FileButton.clicked.connect(lambda: ui.getfile())
ui.GraphItbutton.clicked.connect(lambda: ui.graphit(ui.InputBox.text(),obj))
ui.runalgobutton.clicked.connect(lambda: ui.algorithm(obj))
ui.Algochoicebox.currentTextChanged.connect(lambda: ui.updateboxes())
ui.BackButton.clicked.connect(lambda: ui.backbutton())
ui.BackButton_2.clicked.connect(lambda: ui.backbutton())
ui.BackButton_3.clicked.connect(lambda: ui.backbutton())
sys.exit(app.exec_())