# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UnTangledUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from GraphClass import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 625)
        MainWindow.setStyleSheet("QWidget#MainTab,#VisualINTab,#VisualOUTTab,#DataTab{\n"
"border-image: url(back.jpg) 0 0 0 0 stretch stretch;\n"
"}\n"
"#MainLabel,#Inputlabel,#fileinputlabel,#labelcheckbox,#Graphitlabel,#algolabel,#visualoutputcheckbox,#tabularoutputcheckbox,#Outputgraphlabel,#Outputtablelabel{\n"
"color: white;}\n"
"#InputBox,#FileDatabox{\n"
"background-color: rgba(0, 0, 0, 0); \n"
"color: white;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.Datatable = QtWidgets.QTabWidget(self.centralwidget)
        self.Datatable.setGeometry(QtCore.QRect(-4, -21, 1051, 631))
        self.Datatable.setStyleSheet("\n"
"")
        self.Datatable.setObjectName("Datatable")
        self.MainTab = QtWidgets.QWidget()
        self.MainTab.setStyleSheet("")
        self.MainTab.setObjectName("MainTab")
        self.FileButton = QtWidgets.QPushButton(self.MainTab)
        self.FileButton.setGeometry(QtCore.QRect(630, 210, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.FileButton.setFont(font)
        self.FileButton.setObjectName("FileButton")
        self.Inputlabel = QtWidgets.QLabel(self.MainTab)
        self.Inputlabel.setGeometry(QtCore.QRect(36, 150, 591, 41))
        self.Inputlabel.setObjectName("Inputlabel")
        self.InputBox = QtWidgets.QLineEdit(self.MainTab)
        self.InputBox.setGeometry(QtCore.QRect(300, 210, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.InputBox.setFont(font)
        self.InputBox.setObjectName("InputBox")
        self.MainLabel = QtWidgets.QLabel(self.MainTab)
        self.MainLabel.setGeometry(QtCore.QRect(300, 0, 461, 131))
        self.MainLabel.setStyleSheet("")
        self.MainLabel.setObjectName("MainLabel")
        self.fileinputlabel = QtWidgets.QLabel(self.MainTab)
        self.fileinputlabel.setGeometry(QtCore.QRect(40, 262, 451, 31))
        self.fileinputlabel.setObjectName("fileinputlabel")
        self.FileDatabox = QtWidgets.QTextBrowser(self.MainTab)
        self.FileDatabox.setGeometry(QtCore.QRect(30, 310, 841, 261))
        self.FileDatabox.setObjectName("FileDatabox")
        self.GraphItbutton = QtWidgets.QPushButton(self.MainTab)
        self.GraphItbutton.setGeometry(QtCore.QRect(900, 350, 121, 81))
        self.GraphItbutton.setMouseTracking(False)
        self.GraphItbutton.setStyleSheet("background-colo= qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69))border: 2px dashed black;")
        self.GraphItbutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.GraphItbutton.setIcon(icon)
        self.GraphItbutton.setIconSize(QtCore.QSize(111, 71))
        self.GraphItbutton.setObjectName("GraphItbutton")
        self.Graphitlabel = QtWidgets.QLabel(self.MainTab)
        self.Graphitlabel.setGeometry(QtCore.QRect(900, 430, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Graphitlabel.setFont(font)
        self.Graphitlabel.setObjectName("Graphitlabel")
        self.labelcheckbox = QtWidgets.QCheckBox(self.MainTab)
        self.labelcheckbox.setGeometry(QtCore.QRect(900, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelcheckbox.setFont(font)
        self.labelcheckbox.setObjectName("labelcheckbox")
        self.Datatable.addTab(self.MainTab, "")
        self.VisualINTab = QtWidgets.QWidget()
        self.VisualINTab.setObjectName("VisualINTab")
        self.InputGraph = QtWidgets.QLabel(self.VisualINTab)
        self.InputGraph.setGeometry(QtCore.QRect(30, 10, 981, 441))
        self.InputGraph.setScaledContents(True)
        self.InputGraph.setObjectName("InputGraph")
        self.Algochoicebox = QtWidgets.QComboBox(self.VisualINTab)
        self.Algochoicebox.setGeometry(QtCore.QRect(170, 500, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Algochoicebox.setFont(font)
        self.Algochoicebox.setObjectName("Algochoicebox")
        self.Algochoicebox.addItem("")
        self.Algochoicebox.addItem("")
        self.Algochoicebox.addItem("")
        self.Algochoicebox.addItem("")
        self.Algochoicebox.addItem("")
        self.Algochoicebox.addItem("")
        self.Algochoicebox.addItem("")
        self.algolabel = QtWidgets.QLabel(self.VisualINTab)
        self.algolabel.setGeometry(QtCore.QRect(150, 460, 531, 41))
        self.algolabel.setObjectName("algolabel")
        self.runalgobutton = QtWidgets.QPushButton(self.VisualINTab)
        self.runalgobutton.setGeometry(QtCore.QRect(470, 500, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.runalgobutton.setFont(font)
        self.runalgobutton.setAutoFillBackground(False)
        self.runalgobutton.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("algo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.runalgobutton.setIcon(icon1)
        self.runalgobutton.setIconSize(QtCore.QSize(181, 71))
        self.runalgobutton.setObjectName("runalgobutton")
        self.visualoutputcheckbox = QtWidgets.QCheckBox(self.VisualINTab)
        self.visualoutputcheckbox.setEnabled(True)
        self.visualoutputcheckbox.setGeometry(QtCore.QRect(190, 540, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.visualoutputcheckbox.setFont(font)
        self.visualoutputcheckbox.setObjectName("visualoutputcheckbox")
        self.tabularoutputcheckbox = QtWidgets.QCheckBox(self.VisualINTab)
        self.tabularoutputcheckbox.setEnabled(True)
        self.tabularoutputcheckbox.setGeometry(QtCore.QRect(320, 540, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabularoutputcheckbox.setFont(font)
        self.tabularoutputcheckbox.setObjectName("tabularoutputcheckbox")
        self.BackButton = QtWidgets.QPushButton(self.VisualINTab)
        self.BackButton.setGeometry(QtCore.QRect(890, 510, 121, 61))
        self.BackButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("bkbutton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon2)
        self.BackButton.setIconSize(QtCore.QSize(121, 75))
        self.BackButton.setObjectName("BackButton")
        self.Datatable.addTab(self.VisualINTab, "")
        self.VisualOUTTab = QtWidgets.QWidget()
        self.VisualOUTTab.setObjectName("VisualOUTTab")
        self.OutputGraph = QtWidgets.QLabel(self.VisualOUTTab)
        self.OutputGraph.setGeometry(QtCore.QRect(20, 100, 991, 481))
        self.OutputGraph.setScaledContents(True)
        self.OutputGraph.setObjectName("OutputGraph")
        self.Outputgraphlabel = QtWidgets.QLabel(self.VisualOUTTab)
        self.Outputgraphlabel.setGeometry(QtCore.QRect(20, 0, 791, 81))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Outputgraphlabel.setFont(font)
        self.Outputgraphlabel.setObjectName("Outputgraphlabel")
        self.BackButton_2 = QtWidgets.QPushButton(self.VisualOUTTab)
        self.BackButton_2.setGeometry(QtCore.QRect(900, 20, 121, 61))
        self.BackButton_2.setText("")
        self.BackButton_2.setIcon(icon2)
        self.BackButton_2.setIconSize(QtCore.QSize(121, 75))
        self.BackButton_2.setObjectName("BackButton_2")
        self.Datatable.addTab(self.VisualOUTTab, "")
        self.DataTab = QtWidgets.QWidget()
        self.DataTab.setObjectName("DataTab")
        self.outputtable = QtWidgets.QTableWidget(self.DataTab)
        self.outputtable.setGeometry(QtCore.QRect(60, 100, 911, 481))
        self.outputtable.setObjectName("outputtable")
        self.outputtable.setColumnCount(0)
        self.outputtable.setRowCount(0)
        self.Outputtablelabel = QtWidgets.QLabel(self.DataTab)
        self.Outputtablelabel.setGeometry(QtCore.QRect(60, 0, 791, 91))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.Outputtablelabel.setFont(font)
        self.Outputtablelabel.setObjectName("Outputtablelabel")
        self.BackButton_3 = QtWidgets.QPushButton(self.DataTab)
        self.BackButton_3.setGeometry(QtCore.QRect(900, 20, 121, 61))
        self.BackButton_3.setText("")
        self.BackButton_3.setIcon(icon2)
        self.BackButton_3.setIconSize(QtCore.QSize(121, 75))
        self.BackButton_3.setObjectName("BackButton_3")
        self.Datatable.addTab(self.DataTab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FileButton.setText(_translate("MainWindow", "Browse"))
        self.Inputlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Please choose the file to use for input:</span></p></body></html>"))
        self.MainLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">UnTangled</span></p><p align=\"center\"><span style=\" font-size:16pt;\">A graph and tree visualizer <br/>to process different algorithms</span></p></body></html>"))
        self.fileinputlabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Following is the input provided in the file:</span></p></body></html>"))
        self.Graphitlabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Graph It!</span></p></body></html>"))
        self.labelcheckbox.setText(_translate("MainWindow", "Add Weights \n"
" as Label"))
        self.Datatable.setTabText(self.Datatable.indexOf(self.MainTab), _translate("MainWindow", "Tab 1"))
        self.InputGraph.setText(_translate("MainWindow", "TextLabel"))
        self.Algochoicebox.setItemText(0, _translate("MainWindow", "Prims Algorithm"))
        self.Algochoicebox.setItemText(1, _translate("MainWindow", "Kruskal Algorithm"))
        self.Algochoicebox.setItemText(2, _translate("MainWindow", "Dijkstra Algorithm"))
        self.Algochoicebox.setItemText(3, _translate("MainWindow", "Bellman Ford Algorithm"))
        self.Algochoicebox.setItemText(4, _translate("MainWindow", "Floyd Warshall Algorithm"))
        self.Algochoicebox.setItemText(5, _translate("MainWindow", "Borůvka\'s Algorithm"))
        self.Algochoicebox.setItemText(6, _translate("MainWindow", "Clustering Coefficient in Graph Theory"))
        self.algolabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Please choose an algorithm to run on this graph:</span></p></body></html>"))
        self.runalgobutton.setText(_translate("MainWindow", "Run It"))
        self.visualoutputcheckbox.setText(_translate("MainWindow", "Show Output \n"
" Visually"))
        self.tabularoutputcheckbox.setText(_translate("MainWindow", "Show Output \n"
" in Table"))
        self.Datatable.setTabText(self.Datatable.indexOf(self.VisualINTab), _translate("MainWindow", "Tab 2"))
        self.OutputGraph.setText(_translate("MainWindow", "TextLabel"))
        self.Outputgraphlabel.setText(_translate("MainWindow", "Result Generated by: "))
        self.Datatable.setTabText(self.Datatable.indexOf(self.VisualOUTTab), _translate("MainWindow", "Page"))
        self.Outputtablelabel.setText(_translate("MainWindow", "Result Generated by: "))
        self.Datatable.setTabText(self.Datatable.indexOf(self.DataTab), _translate("MainWindow", "Page"))

    def getfile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", os.getcwd(), "Text files (*.txt)")
        self.InputBox.setText(fname[0])
        inputfile = open(fname[0], "r")
        self.FileDatabox.setText(inputfile.read())
        self.FileDatabox.setStyleSheet("#FileDatabox{\n"
        "background-color: rgba(255, 255, 255, 1); \n"
        "color: black;}" )

    def graphit(self,path,graph):
        self.tabularoutputcheckbox.setVisible(False)
        self.visualoutputcheckbox.setVisible(False)
        graph.ReadFile(path)
        graph.generategraph()
        if(self.labelcheckbox.isChecked()==True):
            graph.savegraph(1)
        else:
            graph.savegraph(0)
        self.Datatable.setCurrentIndex(1)
        self.InputGraph.setPixmap(QtGui.QPixmap("graph.png"))

    def test(self):
        self.tabularoutputcheckbox.setVisible(False)
        self.visualoutputcheckbox.setVisible(False)
        current = self.Algochoicebox.currentText()
        if(current == "Prims Algorithm"):
            self.visualoutputcheckbox.setCheckState(True)
            self.visualoutputcheckbox.setEnabled(False)
            self.tabularoutputcheckbox.setVisible(False)
            self.visualoutputcheckbox.setVisible(True)

        elif(current=="Kruskal Algorithm"):
            self.visualoutputcheckbox.setCheckState(True)
            self.visualoutputcheckbox.setEnabled(False)
            self.tabularoutputcheckbox.setVisible(False)
            self.visualoutputcheckbox.setVisible(True)

        elif(current=="Floyd Warshall Algorithm"):
            self.tabularoutputcheckbox.setCheckState(True)
            self.tabularoutputcheckbox.setEnabled(False)
            self.visualoutputcheckbox.setVisible(False)
            self.tabularoutputcheckbox.setVisible(True)
        elif(current=="Clustering Coefficient in Graph Theory"):
            self.visualoutputcheckbox.setCheckState(False)
            self.visualoutputcheckbox.setCheckState(False)
            self.tabularoutputcheckbox.setVisible(True)
            self.visualoutputcheckbox.setVisible(True)

    def backbutton(self):
        curr = self.Datatable.currentIndex()
        if(curr!=3):
            self.Datatable.setCurrentIndex(curr-1)
        else:
            self.Datatable.setCurrentIndex(curr-2)

    def algorithm(self,graph):
        algorithmchoice = self.Algochoicebox.currentText()
        if(algorithmchoice=="Prims Algorithm"):
            parent = graph.primMST()
            MST = nx.Graph()
            for i in range(graph.nodecount):
                MST.add_node(int(graph.nodeandpos[i][0]), pos=(float(graph.nodeandpos[i][1]), float(graph.nodeandpos[i][2])))
            mstweight=0
            for i in range(1,graph.nodecount):
                MST.add_edge(parent[i],i, weight=float(graph.matrix[i][parent[i]]))
                mstweight += graph.matrix[i][parent[i]]
            plt.clf()
            pos=nx.get_node_attributes(MST,'pos')
            nx.draw_networkx(MST,pos)
            if (self.labelcheckbox.isChecked()==True):
                labels = nx.get_edge_attributes(MST,'weight')
                nx.draw_networkx_edge_labels(MST,pos,edge_labels=labels)
            plt.savefig('MST.png', bbox_inches='tight')
            self.Datatable.setCurrentIndex(2)
            self.Outputgraphlabel.setText("Result Generated by:"  + "Prim's Algorithm" + '\n' + "MST Weight = " + str(mstweight))
            self.OutputGraph.setPixmap(QtGui.QPixmap("MST.png"))

        elif (algorithmchoice=="Kruskal Algorithm"):
            edges = graph.kruskal_algo()
            MST = nx.Graph()
            for i in range(graph.nodecount):
                MST.add_node(int(graph.nodeandpos[i][0]), pos=(float(graph.nodeandpos[i][1]), float(graph.nodeandpos[i][2])))

            mstweight=0
            for i in range(len(edges)):
                MST.add_edge(edges[i][0],edges[i][1], weight=float(edges[i][2]))
                mstweight += edges[i][2]
                
            plt.clf()
            pos=nx.get_node_attributes(MST,'pos')
            nx.draw_networkx(MST,pos)
            if (self.labelcheckbox.isChecked()==True):
                labels = nx.get_edge_attributes(MST,'weight')
                nx.draw_networkx_edge_labels(MST,pos,edge_labels=labels)
            plt.savefig('MST.png', bbox_inches='tight')
            self.Datatable.setCurrentIndex(2)
            self.Outputgraphlabel.setText("Result Generated by:"  + "Kruskal's Algorithm" + '\n' + "MST Weight = " + str(mstweight))
            self.OutputGraph.setPixmap(QtGui.QPixmap("MST.png"))

        elif(algorithmchoice=="Floyd Warshall Algorithm"):
            matrix = graph.floydWarshall()
            self.outputtable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.outputtable.horizontalHeader().setVisible(True)
            self.outputtable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            self.outputtable.setColumnCount(graph.nodecount)
            self.outputtable.setRowCount(graph.nodecount)
            labels = [str(i) for i in range(graph.nodecount)]
            self.outputtable.setHorizontalHeaderLabels(labels)
            self.outputtable.setVerticalHeaderLabels(labels)
            for i in range(graph.nodecount):
                for j in range(graph.nodecount):
                    self.outputtable.setItem(i,j,QtWidgets.QTableWidgetItem(str(round(matrix[i][j],6))))
            self.Datatable.setCurrentIndex(3)
            self.Outputtablelabel.setText( "Result Generated by:"  + " Floyd Warshall Algorithm")
            self.outputtable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        elif(algorithmchoice=="Clustering Coefficient in Graph Theory"):
            local, globa = graph.CLustering()
            self.outputtable.setColumnCount(graph.nodecount)
            self.outputtable.setRowCount(1)
            labels = [str(i) for i in range(graph.nodecount)]
            self.outputtable.setHorizontalHeaderLabels(labels)
            self.outputtable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            for i in range(graph.nodecount):
                    self.outputtable.setItem(0,i,QtWidgets.QTableWidgetItem(str(round(local[i],6))))
            
            self.outputtable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.Datatable.setCurrentIndex(3)
            self.Outputtablelabel.setText("Result Generated by:"  + "Clustering Coeffecient" + '\n' + "Global Average Coeffecient = " + str(globa))

            """ pos=nx.get_node_attributes(graph,'pos')
            nx.draw(graph, pos, with_labels=True, connectionstyle="arc3,rad=0.1")
            min_x = float('inf')
            min_y = float('inf')

            for i in range(len(local)):
                x,y = pos[i]

                if x < min_x:
                    min_x = x
                if y < min_y:
                    min_y = y

                plt.text(x,y+0.03,s=str(round(local[i], 2)), bbox=dict(facecolor='red'),horizontalalignment='center')
            
            plt.text(min_x, min_y-0.009, 'Average Coefficient = ' + str(round(globa, 3)), fontsize = 22, horizontalalignment= "left", verticalalignment = "top")
            plt.savefig("ClusteringCoefficient.png") """

        elif(algorithmchoice=="Bellman Ford Algorithm"):
            distances = graph.BellmanFord()
            self.outputtable.setColumnCount(graph.nodecount)
            self.outputtable.setRowCount(1)
            labels = [str(i) for i in range(graph.nodecount)]
            self.outputtable.setHorizontalHeaderLabels(labels)
            self.outputtable.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            for i in range(graph.nodecount):
                    self.outputtable.setItem(0,i,QtWidgets.QTableWidgetItem(str(round(distances[i],6))))
            self.outputtable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.Datatable.setCurrentIndex(3)
            self.Outputtablelabel.setText("Result Generated by:"  + "Bellman Ford" )

