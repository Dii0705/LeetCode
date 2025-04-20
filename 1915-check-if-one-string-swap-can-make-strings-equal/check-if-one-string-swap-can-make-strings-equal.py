class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # time complexity: O(n)
        if s1 == s2:
            return True
        diff = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff.append(i)
            if len(diff) > 2:
                return False
        if len(diff) == 2:
            # check if swap can help
            i, j = diff
            return s1[i] == s2[j] and s2[i] == s1[j]
        return len(diff) == 0