# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)
        
        sorted_lst = in_order_traversal(root)

        def build_balanced_bst(vals):
            if not vals:
                return None
            mid = len(vals)//2
            root = TreeNode(vals[mid])
            root.left = build_balanced_bst(vals[:mid])
            root.right = build_balanced_bst(vals[mid+1:])
            return root
        
        return build_balanced_bst(sorted_lst)
