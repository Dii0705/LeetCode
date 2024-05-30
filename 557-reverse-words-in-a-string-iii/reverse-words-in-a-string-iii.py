class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseStr(w):
            w = list(w)
            l, r = 0, len(w)-1
            while l < r:
                w[l], w[r] = w[r], w[l]
                l+=1
                r-=1
            return ''.join(w)
        
        words = s.split()
        reversed_words = [reverseStr(word) for word in words]
        return ' '.join(reversed_words) # don't forget the space