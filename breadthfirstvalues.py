class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def bf(root):
    if root == None: return []
    result = []
    stack = [root]
    
    while len(stack) > 0:
        current = stack.pop()
        result.append(current.val)

        if current.left: stack.insert(0, current.left)
        if current.right: stack.insert(0, current.right)
    
    return print(result)

bf(a)