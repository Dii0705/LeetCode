class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        curSet, subSet = [], []

        def helper(i, nums, curSet, subSet):
            if i >= len(nums):
                subSet.append(curSet.copy())
                return
            
            # include the nums[i]
            curSet.append(nums[i])
            helper(i+1, nums, curSet, subSet)
            curSet.pop()

            # not include the nums[i]
            # i.e. we encounter duplicates in the array
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            helper(i+1, nums, curSet, subSet)
        
        helper(0, nums, curSet, subSet)
        return subSet