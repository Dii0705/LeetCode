# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        idx = 0
        cur_max = -float("inf")

        for i in range(len(nums)):
            if nums[i] > cur_max:
                cur_max = nums[i]
                idx = i
        left = self.constructMaximumBinaryTree(nums[:idx])
        right = self.constructMaximumBinaryTree(nums[idx+1:])

        return TreeNode(cur_max, left, right)


