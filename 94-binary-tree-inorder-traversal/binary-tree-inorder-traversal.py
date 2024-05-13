# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(cur):
            if not cur:
                return
            if cur.left:
                traverse(cur.left)
            res.append(cur.val)
            if cur.right:
                traverse(cur.right)
        traverse(root)
        return res