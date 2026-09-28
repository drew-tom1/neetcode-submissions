# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        

        dummy = ListNode(0)
        dummy.next = head
        fast = head
        count = 1

        prev_tail = dummy
        group_tail = head

        while fast:
            if count % k == 0:
                nxt_head = fast.next if fast.next else None
                prev = None
                curr = group_tail
                
                for _ in range(k):
                    nxt_node = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt_node
                
                prev_tail.next = prev
                group_tail.next = nxt_head
                prev_tail = group_tail
                group_tail = nxt_head

                fast = nxt_head
            else:
                fast = fast.next
            count += 1
        
        return dummy.next

        