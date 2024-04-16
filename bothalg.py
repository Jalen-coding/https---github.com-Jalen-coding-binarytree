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

# def bf(root, target):
#     if root == None: return print(False)
#     queue = [ root ]
#     while len(queue) > 0:
#         current = queue.pop()
#         if current.val == target: return print(True)

#         if current.left: queue.insert(0, current.left)
#         if current.right: queue.insert(0, current.right)
    
#     return print(False)

# bf(a, 'e')

# def df_recursion(root, target):
#     if root == None: return print(False)
#     if root.val == target: return print(True)
#     if df_recursion(root.left, target) or df_recursion(root.right, target):
#         return print(True)

# df_recursion(a, 'f')

def df_iterative(root, target):
    if root == None: return print(False)
    stack = [ root ]
    while len(stack) > 0:
        current = stack.pop()
        if current.val == target: return print(True)

        if current.right: stack.insert(0, current.right)
        if current.left: stack.insert(0, current.left)

    return print(False)

df_iterative(a, 'f')