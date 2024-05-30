class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_height = 0
        max_height = 0

        for g in gain:
            current_height += g
            max_height = max(max_height, current_height)
        return max_height