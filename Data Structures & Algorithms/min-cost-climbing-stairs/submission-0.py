class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        def dfs(i, total_cost):
            if i >= len(cost):
                return total_cost


            return min(dfs(i + 1, total_cost + cost[i]), dfs(i + 2, total_cost + cost[i]))
        
        return min(dfs(0,0), dfs(1, 0))
        