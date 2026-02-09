from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = {}

        def searchTree(root: Optional[TreeNode], level: int):
            if not root:
                return
            if level not in levels:
                levels[level] = []
            levels[level].append(root.val)
            searchTree(root.left, level + 1)
            searchTree(root.right, level + 1)
            return

        searchTree(root, 1)

        sol = []
        for _, val in levels.items():
            sol.append(val)
        return sol
