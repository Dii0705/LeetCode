class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # initially positioned at first index
        # each element in nums represents max jump length at that position
        # return True if you can reach the last index, False otherwise
        goal = len(nums) -1

        # start from the last element and going back 
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False
        