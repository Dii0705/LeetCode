class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # time complexity: O(m x n)
        rows = len(text1)
        cols = len(text2)

        cache = {}
        def helper(r,c):
            nonlocal cache

            if r == rows or c == cols:
                return 0
            if (r,c) in cache:
                return cache[(r,c)]
            if text1[r] == text2[c]:
                # if there is a match, we move to the next character in both strings
                cache[(r,c)] = 1 + helper(r+1,c+1)
            else:
                # if there is no match, we will either move to the next character in text1 or text2
                cache[(r,c)] = max(helper(r+1, c), helper(r, c+1))
            
            return cache[(r,c)]
        return helper(0,0)
