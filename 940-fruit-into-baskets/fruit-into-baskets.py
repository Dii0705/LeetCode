class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        basket = defaultdict(int) #automatically initializes any missing keys with a default integer value of 0, preventing KeyError
        total = 0
        for r in range(len(fruits)):
            basket[fruits[r]] += 1

            while len(basket) > 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l += 1
            
            total = max(total, r - l + 1)
        return total
