p = [1,5,8,9,10,17,17,20,24,30]
def CutRod(p, n):
    if n == 0:
        return 0
    q = - 1000
    for i in range(n):
        q = max(q, p[i] + CutRod(p, n - i - 1))

    return q

def MemoizedCutRod(p, n):
    r = [-1000] * len(p)
    return MemoizedCutRodAux(p, n, r)

def MemoizedCutRodAux(p, n, r):
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -1000
        for i in range(n):
            q = max(q, p[i] + MemoizedCutRodAux(p, n - i - 1, r))
    r[n] = q
    return q

def BottomUpCutRod(p, n):
    r = [0] * len(p)
    r[0] = 0
    for j in range(1, n):
        q = -1000
        for i in range(j):
            q = max(q, p[i] + r[j-i-1])
        r[j] = q
    return r

def ExtendedBottomUpCutRod(p, n):
    r = [0] * n
    s = [0] * n
    for j in range(1, n):
        q = -1000
        for i in range(j):
            if q < p[i] + r[j-i-1]:
                q = p[i] + r[j-i-1] # look like relaxation
                s[j] = i + 1 # look like predecessor
        r[j] = q
    return r, s

print(ExtendedBottomUpCutRod(p, 5))
