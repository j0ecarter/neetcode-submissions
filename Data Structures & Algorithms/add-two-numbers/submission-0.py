class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        cur = res
        carry = 0

        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            curTotal = val1 + val2 + carry
            carry = curTotal // 10
            curTotal = curTotal % 10

            cur.next = ListNode(curTotal)
            cur = cur.next

            if l1:  
                l1 = l1.next
            else:
                l1 = None
            
            if l2:
                l2 = l2.next
            else:
                l2 = None
            
        return res.next