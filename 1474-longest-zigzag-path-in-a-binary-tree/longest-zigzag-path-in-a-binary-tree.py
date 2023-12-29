# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxlength = 0
        
        if not root :
            return 0
        # recursively look into each component and direction now
        def zagger(root, isLeft, length):
             # access maxlength in global scope
            if not root:
                return

            nonlocal maxlength
            maxlength = max(maxlength, length)
            if isLeft:
                zagger (root.right, False, length+1)
                zagger (root.left, True, 1)
            else:
                zagger (root.left, True, length+1)
                zagger (root.right, False, 1)
        
        zagger(root, True,0)
        zagger(root, False,0)
        return maxlength