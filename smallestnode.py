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

# def bf(root):
#     if root == None: return 0
#     queue = [ root ]
#     min = float('inf')

#     while len(queue)>0:
#         current=queue.pop()
#         if current.val<min:
#             min=current.val
        
#         if current.left: queue.insert(0, current.left)
#         if current.right: queue.insert(0, current.right)
    
#     return print(min)

# bf(a)

# def df(root):
#     if root == None: return 0
#     stack = [ root ]
#     min = float('inf')

#     while len(stack)>0:
#         current=stack.pop()
#         if current.val<min:
#             min=current.val
        
#         if current.left: stack.append(current.right)
#         if current.right: stack.append(current.left)
    
#     return print(min)

# df(a)

def df_recursion(root):
    if root == None: return 0

    right_min=df_recursion(root.right)
    left_min=df_recursion(root.left)

    return print(root.val)

df_recursion(a)