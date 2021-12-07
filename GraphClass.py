import re
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    nodeandpos=[]
    edges = []
    nodecount=0
    graph = nx.Graph()
    
    def ReadFile(self,path):
        inputfile = open(path, "r")
        inputfile.readline()
        inputfile.readline()
        self.nodecount = int(inputfile.readline())
        inputfile.readline()
        nodeliststr=[]

        for i in range(self.nodecount):
            nodeliststr.append(inputfile.readline())

        for i in range(self.nodecount):
            self.nodeandpos.append(re.findall(r"[-+]?\d*\.\d+|\d+",nodeliststr[i]))

        inputfile.readline()

        while 1==1:
            line = inputfile.readline()
            if line == '\n':
                break
            line = re.findall(r"[-+]?\d*\.\d+|\d+",line)
            node = line[0]
            line=line[1::2]
            i=0
            while i< len(line):
                self.edges.append([node,line[i],line[i+1]])
                i=i+2

    def generategraph(self):

        for i in range(self.nodecount):
            self.graph.add_node(self.nodeandpos[i][0], pos=(float(self.nodeandpos[i][1]), float(self.nodeandpos[i][2])))

        for i in range(len(self.edges)):
            self.graph.add_edge(self.edges[i][0],self.edges[i][1], weight=float(self.edges[i][2])/10000000)
    
    def displaygraph(self,label):
        pos=nx.get_node_attributes(self.graph,'pos')
        nx.draw_networkx(self.graph,pos)
        if (label==1):
            labels = nx.get_edge_attributes(self.graph,'weight')
            nx.draw_networkx_edge_labels(self.graph,pos,edge_labels=labels)
        plt.show()
