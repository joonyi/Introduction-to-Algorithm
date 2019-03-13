import sys
def MatrixChainOrder(p):
    n = len(p)
    m = [[0 for _ in range(n)] for _ in range(n)]
    s= [[0 for _ in range(n)] for _ in range(n)]
    for L in range(2, n): # Multiplication valid for at least two matrices
        for i in range(1, n-L+1):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                # (Ai..Ak) => m[i][k]
                # (Ak+1..Aj) => m[k+1][j]
                # combine both => p[i-1]*p[k]*p[j]
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m[1][n-1]

p = [30, 1, 40, 10, 25]

print("Minimum number of multiplications is " +
      str(MatrixChainOrder(p)))

"""
na na na na na
na 0        goal
na na 0
na na na 0
na na na na 0
"""