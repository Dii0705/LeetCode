class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        # fixed sliding window
        count = 0
        for i in range(len(s)-2):
            window = s[i:i+3]
            if len(set(window)) == 3: # set doesn't take duplicates
                count += 1
        return count
            