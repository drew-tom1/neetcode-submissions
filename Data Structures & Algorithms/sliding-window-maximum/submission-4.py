import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []
        heapq.heapify_max(maxHeap)
        l, r = 0, 0
            
        

        while r < len(nums):
            if (r - l + 1) > k:
                l += 1

            heapq.heappush_max(maxHeap,(nums[r], r))

            while maxHeap[0][1] < l:
                heapq.heappop_max(maxHeap)

            if (r - l + 1) == k:
                res.append(maxHeap[0][0])
            
            r += 1

            

        return res
        





        