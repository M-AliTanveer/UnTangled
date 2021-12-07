import re
import networkx as nx
import matplotlib.pyplot as plt
inputfile = open("input10.txt", "r")
inputfile.readline()
inputfile.readline()
nodecount = int(inputfile.readline())
inputfile.readline()
nodeliststr=[]
nodeandpos=[]
edges = []
for i in range(nodecount):
    nodeliststr.append(inputfile.readline())

for i in range(nodecount):
    nodeandpos.append(re.findall(r"[-+]?\d*\.\d+|\d+",nodeliststr[i]))

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
        edges.append([node,line[i],line[i+1]])
        i=i+2

pass
graph = nx.Graph()

for i in range(nodecount):
    graph.add_node(nodeandpos[i][0], pos=(float(nodeandpos[i][1]), float(nodeandpos[i][2])))

for i in range(len(edges)):
    graph.add_edge(edges[i][0],edges[i][1], weight=float(edges[i][2])/10000000)
pos=nx.get_node_attributes(graph,'pos')
nx.draw_networkx(graph,pos)
labels = nx.get_edge_attributes(graph,'weight')
nx.draw_networkx_edge_labels(graph,pos,edge_labels=labels)
plt.show()


