# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        c1, c2 = l1, l2

        while c1 and c2:
            if not c1.next and c2.next:
                c1.next = ListNode(0, None)

            if not c2.next and c1.next:
                c2.next = ListNode(0, None)

            ps = (c1.val + c2.val)

            if ps >= 10:
                carry = ps % 10

                c1.val = carry
                
                if not c1.next:
                    c1.next = ListNode(1, None)
                else:
                    c1.next.val += 1
            else:
                c1.val = ps

            c1 = c1.next
            c2 = c2.next
        
        return l1

            

        


        