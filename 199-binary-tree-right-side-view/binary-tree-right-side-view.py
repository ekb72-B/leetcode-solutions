# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # add to queue if it is the right only. if there is only a left
        # then add its right child, if both only right
        """
        Notes: Using a level length variable, you can know that you've seen the last of a level.
        This is good because you can do regular iterative bfs but only return a result of
        the rightmost val bc you have a sense of what value is the last.
        Time: O(n)
        Space: O(d)

        """
        if not root:
            return []

        res = []
        que = deque()
        que.append(root)

        while que:
            len_lvl = len(que)

            for i in range(len_lvl):
                curr = que.popleft()

                if i == len_lvl - 1:
                    res.append(curr.val)

                if curr.left:
                    que.append(curr.left)

                if curr.right:
                    que.append(curr.right)

        return res
