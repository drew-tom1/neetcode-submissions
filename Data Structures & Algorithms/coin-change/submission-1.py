class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def solve(r):
            if r == 0:
                return 0
            if r < 0:
                return float("inf")
            if r in memo:
                return memo[r]
            
            memo[r] = 1 + min(solve(r - c) for c in coins)
            return memo[r]
        
        res = solve(amount)
        return -1 if res == float('inf') else res