class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        permutation = []
        checked = [False] * len(nums)

        def dfs():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return
            
            for i in range(len(nums)):
                if not checked[i]:
                    permutation.append(nums[i])
                    checked[i] = True
                    dfs()
                    permutation.pop()
                    checked[i] = False

            
        
        dfs()

        return res
        