# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    Time Complexity: O(n), n = # of nodes
    """

    def isValidSubtree(
        self, root: Optional[TreeNode], max_right: int, min_left: int
    ) -> bool:
        if not root:
            return True
        left = root.left
        valid_left = True  # base case
        if left:
            # check if left within bounds
            if left.val < root.val and left.val > min_left:
                valid_left = self.isValidSubtree(left, root.val, min_left)
            else:
                valid_left = False
        right = root.right
        valid_right = True  # base case
        if right:
            # check if right within bounds
            if right.val > root.val and right.val < max_right:
                valid_right = self.isValidSubtree(right, max_right, root.val)
            else:
                valid_right = False
        return valid_left and valid_right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isValidSubtree(root, float("inf"), float("-inf"))
