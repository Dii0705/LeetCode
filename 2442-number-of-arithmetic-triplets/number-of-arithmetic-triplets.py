class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        num_set = set(nums)
        count = 0
        for i in range(len(nums)):
            if (nums[i] + diff in num_set) and (nums[i] + 2*diff in num_set):
                count += 1
        return count