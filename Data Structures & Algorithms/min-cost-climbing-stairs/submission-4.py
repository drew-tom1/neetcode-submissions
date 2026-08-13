class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        
        def recurse(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = cost[i] + min(recurse(i + 1), recurse(i + 2))

            return cache[i]

        
        return min(recurse(0), recurse(1))