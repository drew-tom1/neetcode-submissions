class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: x * -1, nums))
        heapq.heapify(nums)
        for i in range(k - 1):
            heapq.heappop(nums)
        return -nums[0]
        