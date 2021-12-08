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
                self.edges.append([int(node),int(line[i]),float(line[i+1])])
                i=i+2

    def generategraph(self):

        for i in range(self.nodecount):
            self.graph.add_node(int(self.nodeandpos[i][0]), pos=(float(self.nodeandpos[i][1]), float(self.nodeandpos[i][2])))

        for i in range(len(self.edges)):
            self.graph.add_edge(self.edges[i][0],self.edges[i][1], weight=float(self.edges[i][2])/10000000)
    
    def savegraph(self,label):
        pos=nx.get_node_attributes(self.graph,'pos')
        nx.draw_networkx(self.graph,pos)
        if (label==1):
            labels = nx.get_edge_attributes(self.graph,'weight')
            nx.draw_networkx_edge_labels(self.graph,pos,edge_labels=labels)
        plt.savefig('graph.png', bbox_inches='tight')

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal_algo(self):
        result = []
        i, e = 0, 0
        MST = sorted(self.edges, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.nodecount):
            parent.append(node)
            rank.append(0)
        while e < self.nodecount - 1:
            u, v, w = self.edges[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        return result
    


    
        
