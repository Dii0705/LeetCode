class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # nums have unique elements
        # return all possible subsets (must be subsequent) that does not contain any duplicates
        # solution can be in any order
        curSet, subSet = [],[]

        def helper(i, nums, curSet, subSet):
            if i >= len(nums):
                subSet.append(curSet.copy())
                return
            # decision to include nums[i]
            curSet.append(nums[i])
            helper(i+1, nums, curSet, subSet)
            curSet.pop()  # make sure there is no dup

            # decision not to include nums[i]
            helper(i+1, nums, curSet, subSet)
        
        helper(0, nums, curSet, subSet)
        return subSet
            