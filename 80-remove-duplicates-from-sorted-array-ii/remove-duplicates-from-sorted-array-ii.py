class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # given sorted array, remove duplicates in place such that each appears at most twice
        # the relative order should be kept the same
        l,r = 0,0

        while r < len(nums):
            count = 1
            while r+1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1

            for i in range(min(2, count)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l