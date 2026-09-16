# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]

    def dfs(self, root):
        if not root:
            return [True, 0]
        
        left, right = self.dfs(root.left), self.dfs(root.right)

        if left[0] and right[0]:
            if abs(left[1] - right[1]) <= 1:
                return [True, 1 + max(left[1], right[1])]

        return [False, 0]
            