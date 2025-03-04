class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memoization
        cache = {}
        def helper(i, target):
            nonlocal cache
            if i == len(nums):
                return 1 if target == 0 else 0
            if (i, target) in cache:
                return cache[(i, target)]
            cache[(i, target)] = helper(i+1, target+nums[i]) + helper(i+1, target-nums[i])
            return cache[(i, target)]
        
        return helper(0, target)