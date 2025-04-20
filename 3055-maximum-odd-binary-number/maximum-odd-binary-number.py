class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Time Complexity: O(n)
        count = 0
        for c in s:
            if c == '1':
                count += 1
        # the odd number has a '1' as the least significant number
        # and the max odd binary will have a '1' as its leading number
        return '1' * (count-1) + '0' * (len(s)-count) + '1'