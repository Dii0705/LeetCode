class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break

        if index == -1:
            return word

        lst = list(word)

        l, r = 0, index
        while l < r:
            lst[l], lst[r] = lst[r], lst[l]            
            l += 1
            r -= 1
        return ''.join(lst)