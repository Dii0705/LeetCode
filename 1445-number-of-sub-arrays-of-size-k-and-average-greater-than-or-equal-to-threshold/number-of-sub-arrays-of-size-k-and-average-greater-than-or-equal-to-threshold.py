class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # return the number of sub-arrays of size k
        # the sub-arrays average must be greater than or equal  to threshold
        
        # sliding window
        l = 0
        curSum = sum(arr[l:l+k])
        res = 1 if curSum >= threshold * k else 0
        

        for r in range(k, len(arr)):
            curSum += arr[r] - arr[l]
            if r-l+1 > k :
                l += 1
            
            if curSum >= threshold * k:
                res += 1
        return res