class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        df = [nums[0], max(nums[0], nums[1])]
        i = 2
        while i < len(nums):
            tmp = df[1]
            df[1] = max(df[0] + nums[i], df[1])
            df[0] = tmp
            i += 1
        return df[1]