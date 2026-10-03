# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))


root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(None)

obj =  Solution()
print(obj.maxDepth(root))