class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            maxSub = max(maxSub + nums[i], nums[i])

            res = max(res, maxSub)
        
        return res
        