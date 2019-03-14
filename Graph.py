from collections import defaultdict
import sys
class Vertex(object):
    def __init__(self, name=None, color='white', d=sys.maxsize, pi=None):
        self.name = str(name)
        self.color = color
        self.d = d
        self.pi = pi
        self.f = d

    def __repr__(self):
        repr = [self.name, self.color, self.d, self.pi]
        return str(repr)

class Graph(object):
    def __init__(self):
        self.V = {}
        self.E = defaultdict(list)
        self.W = []

    def __repr__(self):
        repr = ''
        for key, val in self.V.items():
            repr += str(val) + '\n'
        return repr

    def addEdge(self, u, v):
        u, v = str(u), str(v)
        if u not in self.V:
            self.V[u] = Vertex(u)
        if v not in self.V:
            self.V[v] = Vertex(v)
        self.E[u].append(v)

    def addWeight(self, u, v, w):
        u, v = str(u), str(v)
        if u not in self.V:
            self.V[u] = Vertex(u)
        if v not in self.V:
            self.V[v] = Vertex(v)
        self.W.append([u,v,w])

