class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # array may contain duplicates
        nums.sort()

        curSet, subSet = [], []
        def backtrack(i, curSet, subSet):
            if i == len(nums):
                subSet.append(curSet.copy())
                return
            
            curSet.append(nums[i])
            backtrack(i+1, curSet, subSet)
            curSet.pop()
            

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1, curSet, subSet)

        if nums:
            backtrack(0, curSet, subSet)

        return subSet

