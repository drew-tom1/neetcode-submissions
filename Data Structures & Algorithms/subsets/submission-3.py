class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subs = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subs.copy())
                return

            subs.append(nums[i])
            backtrack(i + 1)

            subs.pop()
            backtrack(i + 1)

            

        backtrack(0)


        return res
        