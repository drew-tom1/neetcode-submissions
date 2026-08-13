class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        combination = []
        rt = 0
        

        def dfs(i, total):
            if i >= len(nums): # boundary check
                return
            if total > target: # stop exploring subtrees if curr total is too much.
                return
            if total == target: # check combo sum, append if true
                res.append(combination.copy())
                return

            # explore all decision subtrees of curr index
            combination.append(nums[i])
            dfs(i, total + nums[i])

            # backtracked call with next index and curr total
            combination.pop()
            dfs(i + 1, total)

        dfs(0, rt)

        return res