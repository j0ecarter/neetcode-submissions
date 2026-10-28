# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, l, r):
            if not node:
                return True
            
            cur = node.val
            if (l is not None and cur <= l) or (r is not None and cur >= r):
                return False

            # need some recursive call back to dfs to pass in the left and right nodes
            final = dfs(node.left, l, node.val) and dfs(node.right, node.val, r)
            return final

        return dfs(root, None, None)
