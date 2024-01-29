# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def bstHelper(root, maxval, minval):
            if not root:
                return True
            if root.val <= minval or root.val >=maxval:
                return False
            return (bstHelper(root.left, root.val, minval) and bstHelper(root.right, maxval, root.val) )
        return bstHelper(root, float('inf'), float('-inf'))

        