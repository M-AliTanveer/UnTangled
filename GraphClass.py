import re
import networkx as nx
import matplotlib.pyplot as plt
import sys
from networkx.algorithms.assortativity import neighbor_degree
from networkx.algorithms.cluster import average_clustering
from networkx.classes import graph

from numpy import inf, matrix

class Graph:
    nodeandpos=[]
    edges = []
    nodecount=0
    graph = nx.Graph()
    matrix = [[]] 
    
    def ReadFile(self,path):
        inputfile = open(path, "r")
        inputfile.readline()
        inputfile.readline()
        self.nodecount = int(inputfile.readline())
        inputfile.readline()
        nodeliststr=[]
        self.matrix = [[0 for i in range(self.nodecount)] for j in range(self.nodecount)]
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
                self.edges.append([int(node),int(line[i]),float(line[i+1])/10000000])
                i=i+2
        for k in range(len(self.edges)):
            self.matrix[self.edges[k][0]][self.edges[k][1]]=self.edges[k][2]

        for i in range(self.nodecount):
            for j in range(self.nodecount):
                if self.matrix [ i ] [ j ] != 0 and self.matrix [ j ] [ i ] == 0:
                    self.matrix [ j ] [ i ] = self.matrix [ i ] [ j ]

                if self.matrix [ i ] [ j ] != 0 and self.matrix [ j ] [ i ] != 0:
                    self.matrix [ i ] [ j ] = min( self.matrix [ i ] [ j ], self.matrix [ j ] [ i ])
                    self.matrix [ j ] [ i ] = self.matrix [ i ] [ j ]
        self.edges = []
        for i in range(self.nodecount):
            for j in range(i):
                if self.matrix[i][j] != 0:
                    self.edges.append([i, j, self.matrix[i][j]/10000000])
           
    def generategraph(self):

        for i in range(self.nodecount):
            self.graph.add_node(int(self.nodeandpos[i][0]), pos=(float(self.nodeandpos[i][1]), float(self.nodeandpos[i][2])))

        for i in range(len(self.edges)):
            self.graph.add_edge(self.edges[i][0],self.edges[i][1], weight=float(self.edges[i][2]))
    
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
    
    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.nodecount):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
 
        return min_index

    def primMST(self):

        key = [sys.maxsize] * self.nodecount
        parent = [None] * self.nodecount 
        key[0] = 0
        mstSet = [False] * self.nodecount
 
        parent[0] = -1
 
        for cout in range(self.nodecount):
 
            u = self.minKey(key, mstSet)
 
            mstSet[u] = True
            for v in range(self.nodecount):
 
                if self.matrix[u][v] > 0 and mstSet[v] == False and key[v] > self.matrix[u][v]:
                        key[v] = self.matrix[u][v]
                        parent[v] = u
        
        return parent
        
    def floydWarshall(self):
        dist = list(map(lambda i: list(map(lambda j: j, i)), self.matrix))
        for i in range(self.nodecount):
            for j in range(self.nodecount):
                if(dist[i][j]==0 and i!=j):
                    dist[i][j]=float(inf)
        
        for k in range(self.nodecount):
            for i in range(self.nodecount):
                for j in range(self.nodecount):
                    dist[i][j] = min(dist[i][j],
                                    dist[i][k] + dist[k][j]
                                    )

        return dist

    def CLustering(self):
        local_cluster = [None]*self.nodecount
        for node in self.graph:

            adjacentNodes = []
            indirectly_connected_nodes = []

            for i in self.graph.neighbors(node):
                adjacentNodes.append(i)

            for i in self.graph.neighbors(node):
                for j in self.graph.neighbors(i):
                    if j in adjacentNodes:
                        indirectly_connected_nodes.append(j)


            cluster = 0
            neighbor_count =(float(len(list(self.graph.neighbors(node)))))
            if len(indirectly_connected_nodes):
                cluster =  (float(len(indirectly_connected_nodes)))/((neighbor_count) * (float(len(list(self.graph.neighbors(node)))) - 1))

            local_cluster[node] = cluster

        globa_coeff = sum(local_cluster)

        globa_coeff /= len(local_cluster)
        # print(avg_coefficient)

        return local_cluster,globa_coeff