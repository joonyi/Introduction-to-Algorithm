def SquareMatrixMultiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    return C


A = [[1,2,3],[2,3,4],[3,4,5]]
B = [[4,2,3],[5,7,8],[7,0,8]]
print(SquareMatrixMultiply(A,B))