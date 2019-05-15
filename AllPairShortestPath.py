import sys
def ExtendShortestPath(L, W):
    n = len(L)
    for i in range(n):
        for j in range(n):
            l = L[i][j]
            for k in range(n):
                l = min(l, L[i][k] + W[k][j])
            L[i][j] = l
    return L

def SlowAllPairsShortest(W):
    n = len(W)
    L = W
    ret = [[]]
    for _ in range(2,n):
        ret = ExtendShortestPath(L,W)
    return ret

def FasterAllPairsShortest(W):
    n = len(W)
    L = W
    m = 1
    ret = [[]]
    for _ in range(int(n**0.5)):
        ret = ExtendShortestPath(L, L)
    return ret


inf = sys.maxsize
W = [
        [0,inf,inf,inf,-1,inf],
        [1,0,inf,2,inf,inf],
        [inf,2,0,inf,inf,-8],
        [-4,inf,inf,0,3,inf],
        [inf,7,inf,inf,0,inf],
        [inf,5,10,inf,inf,0]
     ]
# L = [
#         [0,inf,inf,inf,inf],
#         [inf,0,inf,inf,inf],
#         [inf,inf,0,inf,inf],
#         [inf,inf,inf,0,inf],
#         [inf,inf,inf,inf,0]
#      ]
# L = W
# print(ExtendShortestPath(L, W))
# print(SlowAllPairsShortest(W))
print(FasterAllPairsShortest(W))
