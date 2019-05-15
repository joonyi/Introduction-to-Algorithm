import sys
def SquareMatrixMultiply(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = 0
            for k in range(n):
                C[i][j] = C[i][j] + A[i][k] * B[k][j]

    return C

def SquareMatrixMultiplyRecursive(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    def Multiply(A, B, r1, c1, r2, c2, n):
        if n == 1:
            return A[r1][c1] * B[r2][c2]
        else:
            C[0][0] = Multiply(A, B, 0, 0, 0, 0, n//2) \
                      + Multiply(A, B, 0, 1, 1, 0, n//2)
            C[0][1] = Multiply(A, B, 0, 0, 0, 1, n//2) \
                      + Multiply(A, B, 0, 1, 1, 1, n//2)
            C[1][0] = Multiply(A, B, 1, 0, 0, 0, n//2) \
                      + Multiply(A, B, 1, 1, 1, 0, n//2)
            C[1][1] = Multiply(A, B, 1, 0, 0, 1, n//2) \
                      + Multiply(A, B, 1, 1, 1, 1, n//2)

    Multiply(A, B, len(A), len(A), len(A), len(A), len(A))
    return C

inf = sys.maxsize
A = [[1,3],[7,5]]
B = [[6,8],[4,2]]
print(SquareMatrixMultiply(A, B))
print(SquareMatrixMultiplyRecursive(A, B))

