"""
Bucket Sort divides the interval [0,1) into n equal-sized subintervals, or buckets
and then distributes the n input numbers into the buckets.

Since the inputs are uniformly and independently distributed over [0,1), we do not
expect many numbers to fall into each bucket.

To produce the output, we simply sort the numbers in each bucket and then go
through the buckets in order, listing the element each
"""
def BucketSort(A):
    B = {}
    for i in range(10):
        B[i] = []
    for i in range(len(A)):
        idx = int(A[i] * 10)
        B[idx].append(A[i])
    # Sort in each bucket
    for i in range(len(B)):
        if B[i] and len(B[i]) >= 2:
            InsertionSort(B[i])
    # Concatenate the list B[0...n-1] together
    res = []
    for i in range(len(B)):
        if B[i]:
            res.extend(B[i])
    return res

def InsertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        # Insert A[i] into sorted sequence A[1...j-1]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

A = [0.78,0.17,0.39,0.26,0.72,0.94,0.21,0.12,0.23,0.68]
print(BucketSort(A))
