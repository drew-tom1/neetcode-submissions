class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nm = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nm:
                return [nm[complement], i]
            nm[nums[i]] = i
        