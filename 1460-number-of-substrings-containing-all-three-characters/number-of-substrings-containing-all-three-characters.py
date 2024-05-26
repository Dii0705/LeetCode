class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l = 0
        window = defaultdict(int)
        required_char = {"a","b","c"}

        res = 0
        for r in range(len(s)):
            window[s[r]] += 1
            while all(window[char]>0 for char in required_char):
                res += len(s) -r # fixed r pointer
                window[s[l]] -= 1
                l += 1
        return res
