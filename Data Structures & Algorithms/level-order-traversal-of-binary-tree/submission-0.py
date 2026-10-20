# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        resulting = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queueLen = len(queue)
            cur = []
            
            for val in range(queueLen):
                queueVal = queue.popleft()
                cur.append(queueVal.val)
                
                if queueVal.left:
                    queue.append(queueVal.left)
                if queueVal.right:
                    queue.append(queueVal.right)
                    
            resulting.append(cur)

        return resulting
            