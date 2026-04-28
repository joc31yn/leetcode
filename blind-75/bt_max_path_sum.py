# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(n)
        """
        max_val = -10000
        def calcMaxes(root: Optional[TreeNode]) -> int:
            nonlocal max_val
            if not root:
                return 0
            node_val = root.val
            max_left = calcMaxes(root.left)
            max_right = calcMaxes(root.right)
            if max_left > 0 or max_right > 0:
                root.val = node_val + max(max_left, max_right)
            if root.val > max_val:
                max_val = root.val
            if node_val + max_left + max_right > max_val:
                max_val = node_val + max_left + max_right
            return root.val
        calcMaxes(root)
        return max_val
