# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        max_left = 0
        max_right = 0
        self.max_length = 0
        def diamter(root):
            if root is None:
                return 0
            max_left = diamter(root.left)
            max_right =diamter(root.right)

            self.max_length = max((max_left+max_right),self.max_length)

            return 1+max(max_right,max_left)
        diamter(root)   
        return self.max_length

tree = TreeNode()

tree.right = TreeNode(2)
tree.left = TreeNode(3)

obj = Solution()
print(obj.diameterOfBinaryTree(tree))
