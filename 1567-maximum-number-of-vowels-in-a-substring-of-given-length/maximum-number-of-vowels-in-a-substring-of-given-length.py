class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curCount, maxCount = 0, 0
        vowels = {'a','e','i','o','u'}

        # count vowels in initial window
        for i in range(k):
            if s[i] in vowels:
                curCount += 1
        maxCount = curCount

        # sliding window
        l = 0
        for r in range(k,len(s)):
            if s[l] in vowels:
                curCount -= 1
            if s[r] in vowels:
                curCount += 1
            maxCount = max(maxCount, curCount)
            l += 1
        return maxCount