class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # return all possible permutations
        def helper(i, nums):
            if i == len(nums):
                return [[]]
            

            res = []
            perms = helper(i+1, nums) # i.e [[2,3],[3,2]]
            for p in perms:
                for j in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    res.append(pCopy)
            return res
        return helper(0, nums)