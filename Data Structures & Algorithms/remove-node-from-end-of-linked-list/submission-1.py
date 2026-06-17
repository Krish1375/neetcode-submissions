class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node pointing to head
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # 2. Advance right pointer n steps
        for _ in range(n):
            right = right.next
            
        # 3. Move until right reaches the end
        while right:
            left = left.next
            right = right.next
            
        # 4. Remove the node
        left.next = left.next.next
        
        return dummy.next