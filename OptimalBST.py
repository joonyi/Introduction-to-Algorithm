import sys
# Not working, should rework other time
def OptimalBST(p, q, n):
    e = [[0 for _ in range(n)] for _ in range(n)]
    w = [[0 for _ in range(n)] for _ in range(n)]
    root = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        e[i][i] = q[i]
        w[i][i] = q[i]
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            e[i][j] = inf
            w[i][j] = w[i][j-1] + p[j] + q[j]
            for r in range(i, j+1):
                c = 0
                if r > i:
                    c += e[i][r-1]
                if r < j:
                    c += e[r+1][j]
                c += w[i][j]
                if c < e[i][j]:
                    e[i][j] = c
                    root[i][j] = r
    return e

inf = sys.maxsize
p = [0, 15, 10, 5, 10, 20]
q = [5, 10, 5, 5, 5, 10]
keys = [10, 12, 20]
freq = [34, 8, 50]
print(OptimalBST(p, q, len(p)))
