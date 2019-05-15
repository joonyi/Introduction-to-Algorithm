class RedBlackNode(object):
    def __init__(self,key=None):
        self.key = key
        self.left = None
        self.right = None
        self.p = None
        self.color = None

class NilNode(object):
    def __init__(self):
        self.key = None

class RedBlackTree(object):
    def __init__(self, root, nil):
        self.root = root
        self.nil = nil

def RBInsert(T, z):
    '''
    :param T: root of tree
    :param z: key value of node
    :return:
    '''
    # if T.key == None: # create root
    #     T.key = z
    #     return

    y = None
    newNode = RedBlackTree(z)
    x = T
    while x != None:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if z.key < y.key:
        y.left = newNode
    else:
        y.right = newNode
    newNode.left = None
    newNode.right = None
    newNode.color = 'red'
    RBInsertFixedUp(T, newNode)

def RBInsertFixedUp(T, z):
    while z.p.color == 'red':
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == 'red':
                z.p.color = 'black'
                y.color = 'black'
                z.p.p.color = 'red'
                z = z.p.p
            elif z == z.p.right:
                z = z.p
                LeftRotate(T, z)
                z.p.color = 'black'
                z.p.p.color = 'red'
                RightRotate(T, z.p.p)
        else:
            pass

    T.root.color = 'black'

def LeftRotate(T, x):
    y = x.right # set y
    x.right = y.left # turn y.left into x.right subtree
    if y.left != T.nil:
        y.left.p = x
    y.p = x.p # link x parent to y
    if x.p == T.nil:
        T.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x # put x on y left
    x.p = y


def RightRotate(T, x):
    y = x.left
    x.left = y.right
    if y.right != T.nil:
        y.right.p = x
    y.p = x.p
    if x.p == T.nil:
        T.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    y.right = x
    x.p = y



nil = NilNode()
root = RedBlackNode(26)
T = RedBlackTree(root, nil)
pass
