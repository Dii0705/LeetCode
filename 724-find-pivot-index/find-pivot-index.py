class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # pivot index: sum of its left = sum of its right
        total = sum(nums)
        leftSum = 0

        for i, n in enumerate(nums):
            if leftSum == (total - leftSum - n):
                return i
            leftSum += n

        return -1