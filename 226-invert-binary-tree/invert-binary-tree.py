# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # use a queue add all the items you see on a level on it and then
        def inv(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            inv(root.left)
            inv(root.right)
        inv(root)

        return root