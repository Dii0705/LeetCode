class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking technique with Subsets
        curSet, subSet = [], []
        def backtrack(i, curSet):
            if i >= len(nums):
                subSet.append(curSet.copy())
                return
            
            # include nums[i]
            curSet.append(nums[i])
            backtrack(i+1, curSet)
            curSet.pop()

            # not include nums[i]
            backtrack(i+1, curSet)
        backtrack(0, curSet)
        return subSet
