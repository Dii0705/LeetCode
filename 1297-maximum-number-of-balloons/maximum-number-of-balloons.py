class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # count the frequency
        count = Counter(text)

        # min number of instances of "balloon":
        balloon = {
            'b':1,
            'a':1,
            'l':2,
            'o':2,
            'n':1
        }

        # max number of instances of "balloon":
        res = float("inf")
        for char in balloon:
            res = min(res, count[char]//balloon[char])

        return res