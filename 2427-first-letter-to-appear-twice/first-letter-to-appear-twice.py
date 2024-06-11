class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        char_count = {}
        for char in s:
            if char in char_count:
                return char
            char_count[char] = 1