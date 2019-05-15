def CoinGame(A):
    n = len(A)
    # max value first person can collect from a list of i to j
    mv = [[0 for _ in range(n)] for _ in range(n)]
    for size in range(n): # size of array, when size zero, only one element
        for j in range(size, n):
            i = j - size
            a, b, c = 0, 0, 0

            if i + 2 <= j:
                a = mv[i+2][j]
            if i + 1 <= j - 1:
                b = mv[i+1][j-1]
            if i <= j - 2:
                c = mv[i][j-2]

            mv[i][j] = max(A[i] + min(a,b), A[j] + min(b,c))

    return mv

A = [6,9,1,2,16,8]
print(CoinGame(A))