class Solution:
    def pivotInteger(self, n: int) -> int:
        # sum [1,x] = sum [x, n]
        # return x, if no such int exists, return -1
        prefix = []
        curSum = 0
        for i in range(1,n+1):
            curSum += i
            prefix.append(curSum)
        
        for x in range(1, n+1):
            if prefix[x-1] == prefix[n-1] - prefix[x-1] + x:
                return x

        return -1
