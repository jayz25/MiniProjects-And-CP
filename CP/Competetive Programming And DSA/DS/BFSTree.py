from HeightOfBST import *
# Level Order Traversal of Tree is done by using 2 function
# One function to keep track of levels and other sub-function
# which will print nodes in particualr level
# LevelOrderTraversal is Similar to Breadth First Traversal
def PrintLevelOrder(root):
    h = Height(root)
    for i in range(1,h+1):
        PrintGivenLevel(root,i)
def PrintGivenLevel(root,level):
    if root==None:
        return
    if level==1:
        print(root.data)
    elif level>1:
        PrintGivenLevel(root.left,level-1)
        PrintGivenLevel(root.right,level-1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Level Order Traversal Of Given Tree is:")
PrintLevelOrder(root)
