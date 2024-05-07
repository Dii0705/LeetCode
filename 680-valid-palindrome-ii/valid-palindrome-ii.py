class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l+1:r+1], s[l:r]
                # we want to reverse the string, if the reversed return the same string
                # then we know it's a palindrome
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l += 1
            r -= 1
        return True