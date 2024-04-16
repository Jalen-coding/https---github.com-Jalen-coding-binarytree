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

#def depthfirstValues(root):
#    if root == None: return print([])
#    result = []
#    stack = [ root ]
#    while len(stack) > 0:
#        current = stack.pop()
#        result.append(current.val)
#
#        if current.right: stack.append(current.right)
#        if current.left: stack.append(current.left)
#    
#    return print(result)

#depthfirstValues(None)

def df_recursion(root):
    if root == None: return print([])

    left_values = df_recursion(root.right)
    right_values = df_recursion(root.left)

    return print(root.val, left_values, right_values)

df_recursion(a)