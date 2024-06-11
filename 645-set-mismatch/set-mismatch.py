class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            index = abs(num)-1
            if nums[index] < 0:
                ans.append(abs(num))
            else:
                nums[index] = - nums[index]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i+1)
        return ans