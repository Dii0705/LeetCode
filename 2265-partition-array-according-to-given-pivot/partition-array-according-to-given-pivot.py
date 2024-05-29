class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # find the pivot and maintain the relative order of the elements 
        smaller = []
        greater = []
        equal = []
        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)
        return smaller + equal + greater