class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # return total number of subarrays whose sum equals to k
        res = 0
        curSum = 0
        prefixSum = {0:1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
            
        return res