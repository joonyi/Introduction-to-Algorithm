class Node(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def getName(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest, weight=1):
        self.src = src
        self.dest = dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest

class Digraph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def __str__(self):
        result = ''
        for src in self.nodes:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1] # omit final newline
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

graph = Graph()
# s = Node('s')
# r = Node('r')
# v = Node('v')
# w = Node('w')
t = Edge('s', 'r')
# graph.addNode(s)
# graph.addNode(r)
graph.addEdge(t)