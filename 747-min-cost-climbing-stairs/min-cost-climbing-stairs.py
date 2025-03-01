class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dp(n):
            if n < 2:
                return cost[n]
            if n in cache:
                return cache[n]
            
            cache[n] = cost[n] + min(dp(n-1), dp(n-2))
            return cache[n]
        
        return min(dp(len(cost)-1), dp(len(cost)-2))

