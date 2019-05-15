class BST(object):
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

    def InorderTreeWalk(self, x):
        if x != None:
            self.InorderTreeWalk(x.left)
            print(x.key)
            self.InorderTreeWalk(x.right)

    def InorderTreeWalkIter(self, x):
        stack = []
        current = x
        done = 0
        while not done:
            if current != None:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    current = stack.pop()
                    print(current.key)
                    current = current.right
                else:
                    done = 1

    def TreeSearch(self, x, k):
        if x == None or k == x.key:
            return x
        if k < x.key:
            return self.TreeSearch(x.left, k)
        else:
            return self.TreeSearch(x.right, k)

    def IterTreeSearch(self, x, k):
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def TreeMin(self, x):
        while x.left != None:
            x = x.left
        return x

    def TreeMinRecur(self, x):
        if x.left == None:
            return x
        else:
            return self.TreeMinRecur(x.left)

    def TreeMax(self, x):
        while x.right != None:
            x = x.right
        return x

    def TreeMaxRecur(self, x):
        if x.right == None:
            return x
        return self.TreeMaxRecur(x.right)

    def TreeSuccessor(self, x):
        if x.right != None:
            return self.TreeMin(x.right)
        y = x.p
        while y != None and x == y.right:
            x = y
            y = y.p
        return y

    def LeftRotate(self, T, x):
        y = x.right
        x.right = y.left # turn y left subtree to x right subtree
        if y.left != None:
            y.left.p = x
        y.p = x.p # link x parent to y
        if x.p == None:
            T = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x # put x on y's left
        x.p = y

    def RightRotate(self, T, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.p = x
        y.p = x.p
        if x.p == None:
            T = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def Insert(self, T, z):
        if T.key == None: # create root
            T.key = z
            return

        tail = None
        node = BST(z)
        x = T
        while x != None: # x travel to leaf
            tail = x
            if z < x.key:
                x = x.left
            else:
                x = x.right
        node.p = tail

        if node.key < tail.key: # insert node
            tail.left = node
        else:
            tail.right = node

T = BST()
lis = [15,6,18,3,7,17,20,2,4,13,9]
for x in lis:
    T.Insert(T, x)
# T.InorderTreeWalkIter(T)
# a = T.TreeMinRecur(T)
# print(a.key)
# b = T.TreeMaxRecur(T)
# print(b.key)
# print(T.TreeSearch(T, 8))
# print(T.IterTreeSearch(T, 7))
# successor = T.TreeSearch(T, 13)
# T.TreeSuccessor(successor)
# print(successor)
node = T.TreeSearch(T, 18)
T.RightRotate(T, node)
T.InorderTreeWalkIter(T)