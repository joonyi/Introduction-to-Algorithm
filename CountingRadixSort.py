from math import log
def CountingSort(A):
    k = max(A) + 1
    B = [0] * len(A)
    C = [0] * k
    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1
    # C[i] now contains the number of elem equal to i
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    # C[i] now contains the number of elem less than or equal to i
    # Doing reversed so that the sort is stable
    for j in reversed(range(len(A))):
        C[A[j]] = C[A[j]] - 1
        B[C[A[j]]] = A[j]

    return B

# More general counting sort
def CountingSort2(A, d, radix):
    B = [0] * len(A)
    C = [0] * radix
    for i in range(len(A)):
        digit = (A[i]//(radix**d)) % radix
        C[digit] = C[digit] + 1
    for i in range(1, radix):
        C[i] = C[i] + C[i-1]
    for i in range(len(A)-1, -1, -1):
        idx_C = (A[i]//(radix**d)) % radix
        C[idx_C] = C[idx_C] - 1
        B[C[idx_C]] = A[i]

    return B

def RadixSort(A, radix):
    # radix is the base of the number system
    max_digit = int(log(max(A), radix)) + 1
    for i in range(max_digit):
        A = CountingSort2(A, i, radix)

    return A

# A = [2,5,3,0,2,3,0,3]
# A = [6,0,2,0,1,3,4,6,1,3,2]
A = [329, 457, 657, 839, 436, 720, 355]

# print(CountingSort(A))
print(RadixSort(A, 10))