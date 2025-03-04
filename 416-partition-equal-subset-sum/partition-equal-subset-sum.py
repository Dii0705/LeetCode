class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total//2
        return self.helper(0, target, nums, {})
    
    def helper(self, i, target, nums, cache):
        if target==0:
            return True
        if target < 0 or i == len(nums):
            return False
        
        if (i, target) in cache:
            return cache[(i, target)]

        cache[(i, target)] = self.helper(i+1, target, nums, cache) or self.helper(i+1, target-nums[i], nums, cache)

        return cache[(i, target)]