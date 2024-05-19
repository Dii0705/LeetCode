class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums is sorted, remove the duplicates in-place
        # return the number of unique elements in nums
        # and we want to keep the relative order

        # you just need to return the number
        l = 1

        for r in range(1,len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l