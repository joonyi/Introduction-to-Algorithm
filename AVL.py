class AVL(object):
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.h = 1

    def InorderTreeWalk(self, x):
        if x != None:
            self.InorderTreeWalk(x.left)
            print(x.key)
            self.InorderTreeWalk(x.right)

    def Height(self, x):
        if x == None:
            return 0
        return max(self.Height(x.left), self.Height(x.right)) + 1

    def Unbalance(self, x):
        return abs(self.Height(x.left) - self.Height(x.right))

    def Balance(self, x):
        while self.Unbalance(x) > 1:
            if self.Unbalance(x) > 0:
                self.RightRotate(T, x)
            else:
                self.LeftRotate(T, x)
                self.Balance(x.left)
                self.Balance(x.right)

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

        y = None
        newNode = AVL(z)
        x = T
        while x != None:
            y = x
            if newNode.key > y.key:
                x = x.right
            else:
                x = x.left

        if newNode.key > y.key:
            y.right = newNode

        else:
            y.left = newNode

        # while y != T:
        #     y = y.p
        #     if y.left.h > y.right.h + 1:
        #         self.RightRotate(T, y)
        #     if y.right.h > y.left.h + 1:
        #         self.LeftRotate(T, y)
        #     y.h = max(y.left.h, y.right.h) + 1


# Not working
T = AVL()
lis = [15,6,18,3,7,17,20,2,4,13,9]
# lis  = [41,20,65,11,26,50,23,29,55]
for x in lis:
    T.Insert(T, x)

T.InorderTreeWalk(T)
print(T.Height(T.left), T.Height(T.right))