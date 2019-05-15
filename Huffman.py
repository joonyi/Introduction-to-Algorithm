from heapq import heappush, heappop, heapify
from collections import defaultdict
class Node(object):
    def __init__(self, z=None):
        self.freq = z
        self.left = None
        self.right = None
    def __cmp__(self, other):
        return self.freq > other.freq

def Huffman(C, freq):
    n = len(C)
    Q = []
    heapify(C)
    for i in range(n):
        z = Node()
        z.left = heappop(C)
        z.right = heappop(C)
        z.freq = z.left + z.right
        heappush(Q, z)
    return Q


def Huffman2(symb2freq):
    """Huffman encode the given dict mapping symbols to frequency"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    # return heappop(heap)[1:]
    return sorted(heappop(heap)[1:], key=lambda p: (p, len(p[-1])))

# txt = "this is an example for huffman encoding"
# symb2freq = defaultdict(int)
# for ch in txt:
#     symb2freq[ch] += 1
symb2freq = {'a':45, 'b':13, 'c':12, 'd':16, 'e':9, 'f':5}
huff = Huffman2(symb2freq)
print("Key Freq Huffman")
for p in huff:
    print("%s\t%s\t%s" % (p[0], symb2freq[p[0]], p[1]))

s= [[12, 'tall', 'blue', 1],
[2, 'short', 'red', 9],
[4, 'tall', 'blue', 13]]
s = sorted(s, key = lambda x: (x[0],x[3]))
print(s)