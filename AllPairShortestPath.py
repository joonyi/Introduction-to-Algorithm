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

# Not working
def FasterAllPairsShortest(W):
    n = len(W)
    L = W
    m = 1
    while m < n - 1:
        ret = ExtendShortestPath()


inf = sys.maxsize
W = [
        [0,3,8,inf,-4],
        [inf,0,inf,1,7],
        [inf,4,0,inf,inf],
        [2,inf,-5,0,inf],
        [inf,inf,inf,6,0]
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
print(SlowAllPairsShortest(W))

