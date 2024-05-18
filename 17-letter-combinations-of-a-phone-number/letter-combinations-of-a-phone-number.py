class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Given digits from 2-9 inclusive, each digit represents some letters
        # Return all possible letter combinations
        digitMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        def helper(i,curStr,res,digitMap):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitMap[digits[i]]:  # for a in "abc"
                helper(i+1, curStr + c, res, digitMap) 
                # The curStr should be passed by value 
        res = []
        curStr = ""

        if digits:
            helper(0, curStr, res, digitMap)
        return res
