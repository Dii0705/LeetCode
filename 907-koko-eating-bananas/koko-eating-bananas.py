class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canFinish(piles, k, h):
            hours = 0
            # since Koko can only eat 1 pile a time:
            for pile in piles:
                hours += math.ceil(pile/k) # round up
            return hours <= h
        
        # Binary Search
        l,r = 1, max(piles)
        while l < r:
            m = (l+r) //2
            if canFinish(piles,m,h):
                r = m # not-inclusive
            else:
                l = m+1
        return l