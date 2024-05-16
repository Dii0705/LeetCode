class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        # see if there is a loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # find where the loop is
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        