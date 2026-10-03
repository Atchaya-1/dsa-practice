
class tree:

    def __init__(self,val=0,left=0,right=0):
        self.left = left
        self.right = right
        self.val = val
        

    def invertTree(self, root):
        if not root:
          return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
       
root = tree(1)
root.right = tree(2)
root.left = tree(3)

print(root.invertTree(root))