class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        def dp(i): # Backtracking
            if i > n: # check is ONLY for if i == n, otherwise return 0 to end subtree.
                return 0
            if i == n:
                return 1


            return dp(i + 1) + dp(i + 2) # moving in 1s and 2s, check both trees.
        
        res = dp(0)

        return res
        