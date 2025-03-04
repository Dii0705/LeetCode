class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        cache = {}
        def helper(i,total_weight):
            nonlocal cache
            if i == len(stones):
                return abs(total_weight)
            if (i, total_weight) in cache:
                return cache[(i, total_weight)]
            cache[(i, total_weight)] = min(helper(i+1, total_weight+stones[i]), helper(i+1, total_weight-stones[i]))
            return cache[(i, total_weight)]
        return helper(0, 0)