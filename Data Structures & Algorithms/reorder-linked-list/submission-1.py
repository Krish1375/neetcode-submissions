# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None
        
        def reverse_second_half(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next  # Temporarily store the next node
                curr.next = prev       # Reverse the link
                prev = curr            # Move prev forward
                curr = next_node       # Move curr forward
            return prev  # 'prev' is the new head of the reversed list
        
        second_half_reversed = reverse_second_half(second_half)
        
        curr = head
        while second_half_reversed:
            temp1 = second_half_reversed.next
            temp2 = curr.next
            curr.next = second_half_reversed
            curr.next.next = temp2
            second_half_reversed = temp1
            curr = temp2


