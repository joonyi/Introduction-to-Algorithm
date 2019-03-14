import sys
def FloydWarshall(W, PI):
    n = len(W)
    D = W
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # D[i][j] = min(D[i][j], D[i][k] + D[k][j])
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    PI[i][j] = k

    return D, PI

def TransitiveClosure(T):
    n = len(T)
    t = T
    for k in range(n):
        for i in range(n):
            for j in range(n):
                t[i][j] = t[i][j] or (t[i][k] and t[k][j])
    return t

inf = sys.maxsize
W = [
        [0,3,8,inf,-4],
        [inf,0,inf,1,7],
        [inf,4,0,inf,inf],
        [2,inf,-5,0,inf],
        [inf,inf,inf,6,0]
     ]
W2 = [
        [0,inf,3,0],
        [-2,0,inf,1],
        [inf,inf,0,5],
        [inf,4,inf,0]
    ]
# Predecessor
PI2 = [
        [None,None,0,None],
        [1,None,None,1],
        [None,None,None,2],
        [None,3,None,None]
    ]
print(FloydWarshall(W2,PI2))

# 1 if there is path from i to j, else 0
# T = [[1,0,0,0],[0,1,1,1],[0,1,1,0],[1,0,1,1]]
# print(TransitiveClosure(T))

