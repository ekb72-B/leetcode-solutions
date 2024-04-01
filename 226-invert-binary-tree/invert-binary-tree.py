# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # on curr node, swap left and right then go to left then go to right
        curr = root

        if not curr:
            return

        if curr.left and curr.right:
            curr.left,curr.right = curr.right,curr.left
        
        elif curr.left and not curr.right:
            temp = curr.right
            curr.right = curr.left
            curr.left = temp
           
        
        elif not curr.left and curr.right:
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
        
        self.invertTree(curr.left)
        self.invertTree(curr.right)
        
        return root
