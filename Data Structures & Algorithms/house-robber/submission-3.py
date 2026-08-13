class Solution:
    def rob(self, nums: List[int]) -> int:

        cache = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
                
            rob_curr = nums[i] + dfs(i + 2)
            rob_next = dfs(i + 1)
            
            cache[i] = max(rob_curr, rob_next)

            return cache[i]

        return dfs(0)
        