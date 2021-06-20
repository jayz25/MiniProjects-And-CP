class Node:

    def __init__(self,key):
        self.info = key
        self.left = None
        self.right = None

def findMinMax(root,minimum,maximum,hd):
    if root is None:
        return
    if hd < minimum[0]:
        minimum[0] = hd
    elif hd > maximum[0]:
        maximum[0] = hd
    findMinMax(root.left,minimum,maximum,hd-1)
    findMinMax(root.right,minimum,maximum,hd+1)

def printVerticalLine(root, line_no, hd):
    if root is None:
        return 
    if hd == line_no:
        print (root.info, end = " ")
    printVerticalLine(root.left,line_no, hd-1)
    printVerticalLine(root.right,line_no,hd+1)

def verticalOrder(root):
    maximum = [0]
    minimum = [0]
    findMinMax(root,minimum,maximum,0)

    for line_no in range(minimum[0], maximum[0] + 1):
        printVerticalLine(root, line_no, 0)
        print()
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)

print("Vertical Order Of Tree")

verticalOrder(root)