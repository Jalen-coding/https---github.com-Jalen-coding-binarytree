class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

a = Node(3)
b = Node(15)
c = Node(4)
d = Node(4)
e = Node(2)
f = Node(1)

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

# def sum_df(root):
#     if root == None: return print(0)
#     total = 0
#     stack = [ root ]
#     while len(stack) > 0:
#         num=stack.pop()
#         total+=num.val

#         if num.right: stack.append(num.right)
#         if num.left: stack.append(num.left)

#     return print(total)

# sum_df(a)

# def sum_bf(root):
#     if root == None: return print(0)
#     total = 0
#     queue = [ root ]
#     while len(queue) > 0:
#         num=queue.pop()
#         total+=num.val

#         if num.left: queue.insert(0, num.left)
#         if num.right: queue.insert(0, num.right)

#     return print(total)

# sum_bf(a)

def sum_recursion(root):
    if root == None: return 0

    return root.val+sum_recursion(root.left)+sum_recursion(root.right)

sum_recursion(a)