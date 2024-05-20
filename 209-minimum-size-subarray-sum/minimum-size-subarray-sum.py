class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # return the min length of subarray whose sum is greater than or equal to target
        # if sum is greater than or equal to target, shrink the size
        l,curSum = 0,0
        res = float("inf")

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                res = min(res, r-l+1)
                curSum -= nums[l]
                l+=1
        return res if res != float("inf") else 0
            
                
        
        