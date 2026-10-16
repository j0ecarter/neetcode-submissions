# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        existing_nodes = set()
        current = head

        if not current:
            return False

        while current:
            if current in existing_nodes:
                return True
            existing_nodes.add(current)
            current = current.next
        return False


