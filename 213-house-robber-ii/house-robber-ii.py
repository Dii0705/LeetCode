class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base Case
        if len(nums) < 2:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def helper(nums):
            dp = [nums[0], max(nums[0], nums[1])]
            i = 2
            while i < len(nums):
                temp = dp[1]
                dp[1] = max(nums[i] + dp[0], dp[1])
                dp[0] = temp
                i+=1
            return dp[1]
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))