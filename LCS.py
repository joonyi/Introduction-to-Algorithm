def LCS(X, Y):
    m = len(X)
    n = len(Y)

    L = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L

def LCS2(X, Y):
    m = len(X)
    n = len(Y)
    b = [[0 for _ in range(n+1)] for _ in range(m+1)]
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "diagonal"
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 'up'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 'left'
    return b

def PrintLCS(b, X, Y, i, j):
    if b[i][j] == 0:
        return
    if X[i-1] == Y[j-1]:
        PrintLCS(b, X, Y, i-1, j-1)
        print(X[i-1])
    elif b[i-1][j] > b[i][j-1]:
        PrintLCS(b, X, Y, i-1, j)
    else:
        PrintLCS(b, X, Y, i, j-1)

def PrintLCS2(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == 'diagonal':
        PrintLCS2(b, X, i-1, j-1)
        print(X[i-1])
    elif b[i][j] == 'up':
        PrintLCS2(b, X, i-1, j)
    else:
        PrintLCS2(b, X, i, j-1)


# X = 'ABCBDAB'
# Y = 'BDCABA'
X = 'character'
Y = 'retcarahc'
# b = LCS2(X,Y)
# PrintLCS(b, X, len(X), len(Y))
L = LCS(X, Y)
PrintLCS(L, X, Y, len(X), len(Y))