class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # recursive call using subset with curr index
            subset.append(nums[i])
            dfs(i + 1)

            # backtracked recursive call without curr index in subset.
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        
        return res

        