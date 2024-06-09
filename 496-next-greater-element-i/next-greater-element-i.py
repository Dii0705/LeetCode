class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use Monotonic Stack
        res = {}
        stack = []

        for num in reversed(nums2): # we want to keep a strictly decreasing stack
            while stack and stack[-1] <= num:
                stack.pop()
            
            if stack:
                res[num] = stack[-1]
            else:
                res[num] = -1
            
            stack.append(num) 
        
        return [res[num] for num in nums1]