class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1

        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix 
            prefix *= nums[i] # multiplying prefix after excludes the index being processed.

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res


        

        