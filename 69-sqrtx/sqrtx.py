class Solution:
    def mySqrt(self, x: int) -> int:
        # Very similar question to valid perfect Square
        l, r = 1, x
        while l <= r:
            m = (l+r)//2
            if m*m == x:
                return m
            if m*m > x:
                r = m-1
            else:
                l = m+1
        return r
