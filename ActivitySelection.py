def RecurActivitySelect(s, f, k, n, A):
    A.append((s[k], f[k]))
    m = k + 1
    while m < n and s[m] < f[k]:
        m += 1
    if m < n:
        return RecurActivitySelect(s, f, m, n, A)
    else:
        return A

def IterActivitySelect(s, f):
    n = len(s)
    A = [(s[0],f[0])]
    k = 0
    for m in range(k+1,n):
        if s[m] >= f[k]:
            A.append((s[m],f[m]))
            k = m
    return A

s = [1,3,0,5,3,5,6,8,8,2,12]
f = [4,5,6,7,9,9,10,11,12,14,16]
A = []
# Input must be finish time sorted
print(RecurActivitySelect(s, f, 0, len(s), A))
print(IterActivitySelect(s, f))



