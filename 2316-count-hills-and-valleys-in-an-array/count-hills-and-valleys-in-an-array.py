class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0

        for i in range(1, len(nums)-1):
            # skip same height
            if nums[i] == nums[i-1]:
                continue
            left = i-1
            while left >=0 and nums[left]== nums[i]:
                left -= 1
            right = i+1
            while right < len(nums) and nums[right] == nums[i]:
                right += 1
            
            if left >= 0 and right < len(nums):
                if nums[left] < nums[i] > nums[right]: # hill
                    count += 1
                elif nums[left] > nums[i] < nums[right]: # valley
                    count += 1
        return count