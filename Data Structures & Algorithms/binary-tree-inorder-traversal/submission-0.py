# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(nodes):
            if not nodes:
                return None
            
            dfs(nodes.left)
            res.append(nodes.val)
            dfs(nodes.right)
        
        dfs(root)
        return res