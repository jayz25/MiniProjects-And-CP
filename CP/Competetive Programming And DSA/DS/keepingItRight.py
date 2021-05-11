class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None    
def inorder(root):
    elements = []
    if root:
        elements+=inorder(root.left)
        elements.append(root.data)
        elements+=inorder(root.right)
        print(elements)       
        
        

root = Node(1) 
root.left      = Node(2) 
root.right     = Node(3) 
root.left.left  = Node(4) 
root.left.right  = Node(5)
inorder(root)