# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        min_heap = []
        dummy = ListNode(0, None)
        heapq.heapify(min_heap)
        curr = dummy

        for idx, head in enumerate(lists):
            if not head:
                continue
            heapq.heappush(min_heap, (head.val, idx, head))

        while min_heap:
            node = heapq.heappop(min_heap)
            curr.next = node[2]
            curr = curr.next
            if node[2].next:
                next_node = (node[2].next.val, node[1], node[2].next)
                heapq.heappush(min_heap, next_node)

        return dummy.next
