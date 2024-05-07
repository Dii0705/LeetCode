class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        length = min(len(word1), len(word2))
        for i in range(length):
            res = res + word1[i] + word2[i]

        if len(word1) <= len(word2):
            res += word2[len(word1):]
            
        else:
            res += word1[len(word2):]
        
        return res
