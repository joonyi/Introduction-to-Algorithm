import random
# Partition in to left <= pivot, right greater than pivot
def Partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[j], A[i] = A[i], A[j]

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

# Randomly choose a number and mess up the input
def RandomPartition(A, p, r):
    i = random.randint(p, r)
    A[r], A[i] = A[i], A[r]
    return Partition(A, p ,r)

# Return i-th smallest value of distinct elements in a list
def RandomSelect(A, p, r, i):
    if p == r:
        return A[p]
    q = RandomPartition(A, p, r)
    k = q - p + 1
    if i == k: # the pivot is the answer
        return A[q]
    elif i < k:
        return RandomSelect(A, p, q - 1, i)
    else:
        return RandomSelect(A, q + 1, r, i - k)

C = [9,1,0,2,3,4,6,8,7,10,5]
print(RandomSelect(C, 0, len(C)-1, 6))