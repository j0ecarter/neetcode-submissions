# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maximum):
            if not node:
                return 0
            
            cur = node.val
            if cur >= maximum:
                res = 1
            else:
                res = 0
            maximum = max(maximum, cur) # checking to find if the current node is greater than the previous maximum
            res += dfs(node.left, maximum)
            res += dfs(node.right, maximum)
            return res

        return dfs(root, root.val)
