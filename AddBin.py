def AddBin(A, B):
    A = list(reversed(A)) # reverse to have LSB in front
    B = list(reversed(B))
    C = [0] * (len(A) + 1)
    carry = 0
    i = 0
    while i < len(A):
        C[i] = (int(A[i]) + int(B[i]) + carry) % 2 # remainder
        carry = (int(A[i]) + int(B[i]) + carry) // 2 # quotient
        i += 1
    C[i] = carry
    return list(reversed(C))

print(AddBin('101','110'))