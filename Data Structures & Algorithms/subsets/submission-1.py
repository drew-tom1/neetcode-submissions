class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []


        subset = []
        def dfs(i): # index of value to which we are deciding whether to add to subset or not
            if i >= len(nums): # check if out of bounds, recursive basecase.
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i]) 
            dfs(i + 1) 

            # decision to exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
