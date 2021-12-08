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
sys.exit(app.exec_())


""" if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.tabWidget.setCurrentIndex(0)

    ui.Chapter2Button.clicked.connect(lambda: ui.MovetoChapter2(MainWindow))
    ui.Chapter3Button.clicked.connect(lambda: ui.MovetoChapter3(MainWindow))
    ui.Chapter5Button.clicked.connect(lambda: ui.MovetoChapter5(MainWindow))
    ui.Chapter4Button.clicked.connect(lambda: ui.MovetoChapter4(MainWindow))

    ui.Chp2startbutton.clicked.connect(lambda: ui.Chapter2Start(MainWindow))
    ui.Chp2mainback.clicked.connect(lambda: ui.MovetoMain(MainWindow))
    ui.Chp2iterback.clicked.connect(lambda: ui.MovetoChapter2(MainWindow))
    ui.Chp2choicebox.currentIndexChanged.connect(lambda: ui.Chp2ChoiceChanged(MainWindow))
    
    ui.StartInterpolationButton.clicked.connect(lambda: ui.Chapter3Start(MainWindow))
    ui.Chp3pointsbox.currentIndexChanged.connect(lambda: ui.Chp3pointschanged(MainWindow))
    ui.Chp3mainback.clicked.connect(lambda: ui.MovetoMain(MainWindow))
    ui.Chp3iterback.clicked.connect(lambda: ui.MovetoChapter3(MainWindow))
    ui.Ch3choicebox.currentIndexChanged.connect(lambda: ui.Chp3ChoiceChanged(MainWindow))

    ui.Ch4choicebox.currentIndexChanged.connect(lambda: ui.Chapter4MethodChanged(MainWindow))
    ui.Chp4pointsbox.currentIndexChanged.connect(lambda: ui.Chapter4pointschanged(MainWindow))
    ui.Ch4StartButton.clicked.connect(lambda: ui.Chapter4Start(MainWindow))
    ui.Chp4mainback.clicked.connect(lambda: ui.MovetoMain(MainWindow))
    ui.Ch4iterback.clicked.connect(lambda: ui.MovetoChapter4(MainWindow))

    ui.Ch5StartButton.clicked.connect(lambda: ui.Chapter5Start(MainWindow))
    ui.Chp5mainback.clicked.connect(lambda: ui.MovetoMain(MainWindow))
    ui.Ch5AnsBackButton.clicked.connect(lambda:ui.MovetoChapter5(MainWindow))

    sys.exit(app.exec_()) """