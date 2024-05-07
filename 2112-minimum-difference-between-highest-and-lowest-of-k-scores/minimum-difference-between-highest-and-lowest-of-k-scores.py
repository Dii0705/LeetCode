class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # using sliding window technique

        nums.sort()
        l,r = 0, k-1 # k size window
        res = float("inf")
        
        while r<len(nums):
            res = min(res, nums[r]-nums[l])
            l,r = l+1, r+1
        return res