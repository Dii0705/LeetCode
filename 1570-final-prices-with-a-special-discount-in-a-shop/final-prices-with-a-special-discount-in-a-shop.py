class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = prices[:]
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                index = stack.pop()
                ans[index] = prices[index] - prices[i]
            stack.append(i)
        return ans


