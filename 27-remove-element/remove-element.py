class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # you can't use extra space in this question
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1 # similar to partition algorithm
        return k