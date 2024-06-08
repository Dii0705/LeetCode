class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # assume the majority element always existed
        count = 0
        candidate = nums[0]
        for num in nums:
            if count == 0:
                candidate = num # reset
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate 