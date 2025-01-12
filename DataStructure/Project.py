import matplotlib.pyplot as plt
import networkx as nx


# ..........function....................................................................................................

# ..........structure.......................................
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

# ..........insert.to.tree..................................
def insert(arr, root, i, length):
    if i < length:
        if arr[i] is not None:
            temp = Node(arr[i])
            root = temp
            root.left = insert(arr, root.left, 2 * i + 1, length)
            root.right = insert(arr, root.right, 2 * i + 2, length)
    return root

# ..........pre.order.navigation............................
def preorder(root):
    if root:
        print(root.value, end=' ')
        preorder(root.left)
        preorder(root.right)

# ..........in.order.navigation.............................
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=' ')
        inorder(root.right)

# ..........post.order.navigation...........................
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=' ')

# ..........make.graph......................................
def add_edges(G, root, pos={}, x=0, y=0, layer=1):
    if root:
        pos[root.value] = (x, y)
        if root.left:
            G.add_edge(root.value, root.left.value)
            l = x - 1 / layer
            add_edges(G, root.left, pos, x=l, y=y - 1, layer=layer + 1)
        if root.right:
            G.add_edge(root.value, root.right.value)
            r = x + 1 / layer
            add_edges(G, root.right, pos, x=r, y=y - 1, layer=layer + 1)
    return G, pos

# ..........main........................................................................................................

# ..........input...........................................

data = []
while True:
    d = input("Enter data for tree (for finish enter 'exit'): ").strip()
    if d == 'exit':
        break
    if d:
        data.append(d)
    else:
        data.append(None)

# ..........make.tree.......................................

n = len(data)
root = None
root = insert(data, root, 0, n)

# ..........make.graph......................................

G = nx.Graph()
G, pos = add_edges(G, root)

fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, node_size=500, node_color="skyblue", ax=ax)

# ..........output..........................................

while True:
    ans = input("Enter type of navigation (preorder, inorder, postorder and for finish enter 'exit'): ")

    if ans in ['preorder', 'inorder', 'postorder', 'show', 'exit']:
        if ans == 'preorder':
            print("PreOrder Navigation: ", end='')
            preorder(root)
            print()
        elif ans == 'inorder':
            print("InOrder Navigation: ", end='')
            inorder(root)
            print()
        elif ans == 'postorder':
            print("PostOrder Navigation: ", end='')
            postorder(root)
            print()
        elif ans == 'show':
            plt.show()
        elif ans == 'exit':
            break
    else:
        print("Please enter a valid order!")