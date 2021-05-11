class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def printInorder(root):
    if root:
        printInorder(root.left)
        print(root.data,end=" ")
        printInorder(root.right)

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data,end=" ")
def printPreorder(root):
    if root:
        print(root.data,end= " ")
        printPreorder(root.left)
        printPreorder(root.right)

root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5)
print("Preorder Traversal ")
printPreorder(root)
print("Postorder Traversal")
printPostorder(root)
print("Inorder Traversal")
printInorder(root)