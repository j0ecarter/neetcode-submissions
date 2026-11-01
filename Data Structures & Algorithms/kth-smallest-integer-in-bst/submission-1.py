# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.countVal = k
        
        def dfs(node):
            if not node:
                return None
            
            left_result = dfs(node.left)
            if left_result is not None:
                return left_result

            self.countVal -= 1
            if self.countVal == 0:
                return node.val
            return dfs(node.right)
        
        return dfs(root)
