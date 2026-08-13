"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        clone = defaultdict(lambda: Node(0))
        clone[None] = None
        curr = head

        while curr:
            clone[curr].val = curr.val
            clone[curr].next = clone[curr.next]
            clone[curr].random = clone[curr.random]
            curr = curr.next
        
        return clone[head]
            
            

            

        
        
        

        