# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if not tree1 and not tree2:
            return True
        if not tree1 or not tree2:
            return False
        if tree1.val != tree2.val:
            return False
        return self.isSameTree(tree1.left, tree2.left) and self.isSameTree(
            tree1.right, tree2.right
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time Complexity: O(n * m)
        """
        # restrictions of questions guarantee subRoot is not null
        # if that were not the case just need to add:
        #   if not subRoot:
        #       return True
        # as null can count as subtree of any tree (might need to ask
        # for clarification about this but generally this is accepted)
        if not root:
            return False
        check_root = self.isSameTree(root, subRoot)
        if not check_root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(
                root.right, subRoot
            )
        return True
