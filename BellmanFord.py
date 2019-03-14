import sys
from Graph import Graph
def InitializeSingleSource(G, s):
    for u in G.V.values():
        u.d = sys.maxsize
        u.pi = None
    s.d = 0

def BellmanFord(G, s):
    InitializeSingleSource(G, s)
    for _ in range(len(G.V) - 1):
        for u, v, w in G.W:
            u = G.V[u]
            v = G.V[v]
            if v.d > u.d + w: # Relaxation
                v.d = u.d + w

    for u, v, w in G.W:
        u = G.V[u]
        v = G.V[v]
        if v.d > u.d + w:
            print("Negative Cycle")
            return False
    return True

G = Graph()
G.addWeight('s','t',6)
G.addWeight('s','y',7)
G.addWeight('t','x',5)
G.addWeight('t','y',8)
G.addWeight('t','z',-4)
G.addWeight('y','x',-3)
G.addWeight('y','z',9)
G.addWeight('x','t',-2)
G.addWeight('z','s',8)
G.addWeight('z','x',7)
s = G.V['s']
BellmanFord(G,s)
