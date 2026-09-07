# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiam = 0

        def dfs(current):
            if not current:
                return 0
            
            left = dfs(current.left)
            right = dfs(current.right)

            self.maxDiam = max(self.maxDiam, left + right)
            return max(left, right) + 1
        
        dfs(root)
        return self.maxDiam
