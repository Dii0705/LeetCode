class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # return the number of sub-arrays of size k
        # the sub-arrays average must be greater than or equal  to threshold
        
        # sliding window
        curSum = sum(arr[:k-1])
        res = 0
        
        for l in range(len(arr)-k+1):
            curSum += arr[l+k-1] # add value of "r"
            if curSum >= threshold * k:
                res += 1
            curSum -= arr[l]

        return res
        

        