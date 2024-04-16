class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(23)
b = Node(5)
c = Node(90)
d = Node(19)
e = Node(13)
f = Node(53)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def df_recursion(root):
    if root == None: return float('-inf')
    if root.left==None and root.right==None: return root.val
    maxchild=max(df_recursion(root.left), df_recursion(root.right))
    return root.val + maxchild

df_recursion(a)