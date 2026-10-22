# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return []

        def dfs(cur, depth):
            if not cur:
                return None
            if depth == len(res):
                res.append(cur.val)
            
            dfs(cur.right, depth+1)
            dfs(cur.left, depth+1)
        
        dfs(root, 0)
        return res

            
        
        