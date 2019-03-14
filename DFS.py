import sys
from Graph import Graph
def DFS(G):
    for u in G.V.values():
        u.color = 'white'
        u.pi = None
    time = 0
    for u in G.V.values():
        if u.color == 'white':
            DfsVisit(G, u, time)

def DfsVisit(G, u, time):
    time += 1
    u.d = time
    u.color = 'gray'
    for adj in G.E[u.name]:
        v = G.V[adj]
        if v.color == 'white':
            v.pi = u
            DfsVisit(G, v, time)

    u.color = 'black'
    time += 1
    u.f = time

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
DFS(G)
print(G)