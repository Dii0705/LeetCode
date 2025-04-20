class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # time complexity: O(n)
        min1, min2 = float('inf'), float('inf')
        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min1, min2 = min1, p
        if min1 + min2 <= money:
            return money - min1 - min2
        return money