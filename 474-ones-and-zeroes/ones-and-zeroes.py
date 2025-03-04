class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Memoization
        cache = {}

        def helper(i, m, n):
            nonlocal cache
            if i == len(strs):
                return 0
            if (i, m, n) in cache:
                return cache[(i,m,n)]
            
            zeros = strs[i].count('0')
            ones = strs[i].count('1')

            if zeros <= m and ones <= n:
                # keep or skip
                cache[(i, m, n)]= max(1+helper(i+1, m-zeros, n-ones), helper(i+1, m, n))
            else:
                cache[(i,m, n)] = helper(i+1, m, n)
            
            return cache[i,m,n]
        return helper(0, m, n)