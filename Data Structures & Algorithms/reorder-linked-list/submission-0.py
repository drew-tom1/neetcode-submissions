# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        curr = head
        prev = None

        slow, fast = curr, curr.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        slow = second_half

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        while prev:
            curr_next, prev_next = curr.next, prev.next

            curr.next = prev
            prev.next = curr_next
            curr = curr_next
            prev = prev_next
            
            
            



        