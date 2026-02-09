# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isDescendant(self, root: "TreeNode", node: "TreeNode") -> bool:
        if not root:
            return False
        if root.val == node.val:
            return True
        return (
            self.isDescendant(root.left, node)
            or self.isDescendant(root.right, node)
        )

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Time Complexity: O(h) where h is height of binary tree
        """
        if root.val == p.val or root.val == q.val:
            return root
        p_left_child = self.isDescendant(root.left, p)
        q_left_child = self.isDescendant(root.left, q)
        if p_left_child != q_left_child:
            return root
        # search left subtree
        if p_left_child is True and q_left_child is True:
            return self.lowestCommonAncestor(root.left, p, q)
        # search right subtree
        return self.lowestCommonAncestor(root.right, p, q)
