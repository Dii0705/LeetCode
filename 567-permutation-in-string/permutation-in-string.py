class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        countS1 = collections.Counter(s1)
        window = collections.Counter(s2[:len(s1)-1]) # a window of the size of s1 
        for i in range(len(s1) -1, len(s2)):
            window[s2[i]] += 1

            if window == countS1:
                return True
            
            # decrement count that moves out of the window
            window[s2[i-len(s1)+1]] -= 1 if window[s2[i-len(s1)+1]] != 0 else 0

        return False


