import sys
from Graph import Graph, Vertex

def BFS(G, s):
    for key, u in G.V.items():
        u.color = 'white'
        u.d = sys.maxsize
        u.pi = None
    s.color = 'gray'
    s.d = 0
    s.pi = None
    Q = [s]
    # Q.append(s)
    while Q:
        u = Q.pop(0)
        for adj in G.E[u.name]:
            v = G.V[adj]
            if v.color == 'white':
                v.color = 'gray'
                v.d = u.d + 1
                v.pi = u
                Q.append(v)
        u.color = 'black'

def PrintPath(G, s, v):
    if v.name == s.name:
        print(s)
    elif v.pi == None:
        print('No path from s to v')
    else:
        PrintPath(G, s, v.pi)
        print(v)

G = Graph()
G.addEdge('s','r')
G.addEdge('s','w')
G.addEdge('r','v')
G.addEdge('w','t')
G.addEdge('w','x')
G.addEdge('x','t')
G.addEdge('x','u')
G.addEdge('x','y')
G.addEdge('t','u')
G.addEdge('u','y')
s = G.V['s']
v = G.V['y']
BFS(G,s)
print(G)
PrintPath(G,s,v)