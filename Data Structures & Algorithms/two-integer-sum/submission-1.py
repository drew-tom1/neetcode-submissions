class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        val = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    val.append(i)
                    val.append(j)
                    return val 