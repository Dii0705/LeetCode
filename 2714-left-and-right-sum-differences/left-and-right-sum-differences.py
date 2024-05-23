class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = []
        runningSum = 0
        for num in nums:
            runningSum += num
            prefix.append(runningSum)
        
        res = []
        total = prefix[-1]
        for i in range(len(nums)):
            leftSum = prefix[i-1] if i >0 else 0
            rightSum = total - prefix[i]
            res.append(abs(leftSum-rightSum))
        return res