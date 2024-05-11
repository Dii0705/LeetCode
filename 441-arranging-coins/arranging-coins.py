class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n
        res = 0

        while l <= r:
            m = (l+r) // 2
            coins = (m/2) * (m+1) # applied Gauss Formula to caculate how many coins to complete m rows
            if coins > n: # too high
                r = m-1
            else: 
                l = m+1
                res = max(res,m)
        return res