def SegmentsIntersect(p1, p2, p3, p4):
    d1 = Direction(p3, p4, p1)
    d2 = Direction(p3, p4, p2)
    d3 = Direction(p1, p2, p3)
    d4 = Direction(p1, p2, p4)
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
        ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 == 0 and OnSegment(p3, p4, p1):
        return True
    elif d2 == 0 and OnSegment(p3, p4, p2):
        return True
    elif d3 == 0 and OnSegment(p1, p2, p3):
        return True
    elif d4 == 0 and OnSegment(p1, p2, p4):
        return True
    else:
        return False

def Direction(pi, pj, pk):
    xi, yi = pi[0], pi[1]
    xj, yj = pj[0], pj[1]
    xk, yk = pk[0], pk[1]
    return (xj - xi) * (yk - yi) - (xk - xi) * (yj - yi)

def OnSegment(pi, pj, pk):
    xi, yi = pi[0], pi[1]
    xj, yj = pj[0], pj[1]
    xk, yk = pk[0], pk[1]
    if min(xi, xj) <= xk <= max(xi, xj) and min(yi, yj) <= yk <= max(yi, yj):
        return True
    else:
        return False

p3 = (2,2)
p1 = (1,4)
p2 = (4,3)
p4 = (5,5)

print(SegmentsIntersect(p1,p2,p3,p4))