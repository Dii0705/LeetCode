class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # return the size of longest subarray containing only 1's 
        # return 0 if no such subarray
        zero_count = 0
        max_len = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count += 1
            
            while zero_count > 1: # at most one 0 (because we can delete one element)
                if nums[l] == 0:
                    zero_count -=1
                l+= 1
            max_len = max(max_len, r-l)
        
        return max_len