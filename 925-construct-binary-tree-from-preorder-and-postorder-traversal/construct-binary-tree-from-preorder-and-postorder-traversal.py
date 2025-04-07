# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
                
        root = TreeNode(preorder[0])

        if len(preorder) == 1:
            return root
        left_root = preorder[1]
        
        # left root index in the postorder array
        left_root_index = postorder.index(left_root)
        left_subtree_size = left_root_index + 1

        # Reorganize the tree
        left_preorder = preorder[1:left_subtree_size+1]
        right_preorder = preorder[left_subtree_size+1:]

        left_postorder = postorder[:left_root_index+1]
        right_postorder = postorder[left_root_index+1:-1]

        # construct the tree
        root.left = self.constructFromPrePost(left_preorder, left_postorder)
        root.right = self.constructFromPrePost(right_preorder, right_postorder)

        return root