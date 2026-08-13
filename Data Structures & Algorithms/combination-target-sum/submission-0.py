class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        curr_amt = 0
        combination = []

        def dfs(i, rt):
            # recursive base cases
            if rt > target or i >= len(nums):
                return
            if rt == target:
                res.append(combination.copy())
                return
            
            combination.append(nums[i])
            dfs(i, rt + nums[i])
            combination.pop()

            dfs(i + 1, rt)
        

        dfs(0, curr_amt)

        return res