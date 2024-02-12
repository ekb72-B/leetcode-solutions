# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        que = []
        que.append(root)
        res = []

        while que:
            lenq = len(que)
            list1 = []
            for i in range(lenq):
                node = que.pop(0)
                if node:
                    list1.append(node.val)
                    que.append(node.left)
                    que.append(node.right)

            if list1:
                res.append(sum(list1)/len(list1))
        
        return res
    
            
        