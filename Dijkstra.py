import sys
from Graph import Graph
def InitializeSingleSource(G, s):
    for u in G.V.values():
        u.d = sys.maxsize
        u.pi = None
    s.d = 0

def ExtractMin(Q):
    u = Q[0]
    index = 0
    for i, v in enumerate(Q):
        if v.d < u.d:
            u = v
            index = i
    Q.pop(index)
    return u

# Wrong
def Dijkstra(G,s):
    InitializeSingleSource(G, s)
    Q = []
    for u in G.V.values():
        Q.append(u)
    while Q:
        node = ExtractMin(Q)
        for u, v, w in G.W:
            u = G.V[u]
            v = G.V[v]
            if v.d > u.d + w: # Relaxation
                v.d = u.d + w
                v.pi = u

G = Graph()
G.addWeight('s','t',10)
G.addWeight('s','y',5)
G.addWeight('t','x',1)
G.addWeight('t','y',2)
G.addWeight('y','t',3)
G.addWeight('y','x',9)
G.addWeight('y','z',2)
G.addWeight('x','z',4)
G.addWeight('z','s',7)
G.addWeight('z','x',6)
s = G.V['s']
Dijkstra(G,s)
print(G)