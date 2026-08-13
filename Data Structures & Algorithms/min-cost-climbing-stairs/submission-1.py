class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = [-1] * len(cost)

        def dfs(i, total_cost):
            if i >= len(cost):
                return total_cost
            if cache[i] != -1:
                return cache[i]
            
            # no need to add cost to total_cost in dfs call bc we are already returning the sum.
            one_step = cost[i] + dfs(i + 1, total_cost) 
            two_step = cost[i] + dfs(i + 2, total_cost)

            cache[i] = min(one_step, two_step)

            return cache[i]
        
        return min(dfs(0,0), dfs(1, 0))
        