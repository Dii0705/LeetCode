class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        def maxConsecutiveChar(ch:str) -> str:
            l = 0
            max_count = 0
            count = 0
            for r in range(len(answerKey)):
                if answerKey[r] == ch:
                    count += 1
                while (r-l+1) - count > k:
                    if answerKey[l] == ch: 
                        count -= 1
                    l += 1
                max_count = max(max_count, r-l+1)
            return max_count
        return max(maxConsecutiveChar("T"), maxConsecutiveChar("F"))
