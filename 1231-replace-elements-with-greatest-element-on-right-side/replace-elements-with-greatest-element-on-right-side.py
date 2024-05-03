class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse iteration
        # newMax = max(arr[i+1], prevMax)
        prevMax = -1

        for i in range(len(arr)-1, -1, -1):
            newMax = max(arr[i], prevMax)
            arr[i] = prevMax
            prevMax = newMax
        return arr