# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Time Complexity: O(k + h)
        """
        def kthLeftSmallest(root: Optional[TreeNode]) -> int:
            nonlocal k
            temp = root
            leftNodes = []
            sol = -1
            while temp:
                leftNodes.append(temp)
                temp = temp.left
            for i in range(len(leftNodes) - 1, -1, -1):
                leftMost = leftNodes[i]
                if k == 1:
                    sol = leftMost.val
                    break
                k -= 1
                if leftMost.right:
                    val = kthLeftSmallest(leftMost.right)
                    # kth in right subtree
                    if val != -1:
                        sol = val
                        break
            return sol

        return kthLeftSmallest(root)
