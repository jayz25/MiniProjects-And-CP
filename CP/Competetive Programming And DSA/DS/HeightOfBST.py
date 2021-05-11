class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def Height(node):
    if node==None:
        return 0
    left_height = Height(node.left)
    right_height = Height(node.right)
    return 1 + max(left_height,right_height)


'''root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
print(Height(root))'''