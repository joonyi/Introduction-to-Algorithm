class LinkedList(object):
    def __init__(self, key=None, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

        if self.key == None:
            self.prev = self
            self.next = self

def ListSearch(L, k):
    x = L.next
    while x != L and x.key != k:
        x = x.next
    if x.key:
        return x
    else:
        return None

def ListInsert(L, x):
    # Insert in the head
    # Put x between L and L.next
    x.next = L.next
    L.next.prev = x
    # Update connection of L and x
    L.next = x
    x.prev = L

def ListDelete(L, x):
    x.prev.next = x.next
    x.next.prev = x.prev

def PrintList(L):
    x = L.next
    while x != L:
        print(x.key, end='\t')
        x = x.next
    print()

# A = [25, 9,16,4,1]
# L = LinkedList() # Sentinel
# for i in A:
#     ListInsert(L, LinkedList(i))
# PrintList(L)
# x = ListSearch(L, 16)
# ListDelete(L, x)
# PrintList(L)