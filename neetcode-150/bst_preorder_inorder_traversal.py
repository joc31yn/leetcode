# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     """
#     Works but not efficient
#     """
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         root_val = preorder[0]
#         new_bst = TreeNode(root_val)
#         if len(preorder) == 1:
#             return new_bst
#         lefts = set()
#         rights = set()
#         foundMiddle = False
#         root_index = 0
#         for i, o in enumerate(inorder):
#             if o == root_val:
#                 foundMiddle = True
#                 root_index = i
#                 continue
#             if not foundMiddle:
#                 lefts.add(o)
#             else:
#                 rights.add(o)

#         firstLeft = -1
#         firstRight = -1
#         for p in preorder:
#             if p in lefts and firstLeft == -1:
#                 firstLeft = p
#             if p in rights and firstRight == -1:
#                 firstRight = p
#             if firstLeft != -1 and firstRight!= -1:
#                 break

#         new_left_preorder = [x for x in preorder if x in lefts]
#         new_left_inorder = []
#         for i in inorder:
#             if i != root_val:
#                 new_left_inorder.append(i)
#             else:
#                 break

#         new_right_preorder = [x for x in preorder if x in rights]
#         new_right_inorder = []
#         for i, o in enumerate(inorder):
#             if i > root_index:
#                 new_right_inorder.append(o)

#         if new_left_preorder and new_right_preorder:
#             new_bst.left = self.buildTree(new_left_preorder, new_left_inorder)
#             new_bst.right = self.buildTree(new_right_preorder, new_right_inorder)
#         elif new_left_preorder:
#             new_bst.left = self.buildTree(new_left_preorder, new_left_inorder)
#         elif new_right_preorder:
#             new_bst.right = self.buildTree(new_right_preorder, new_right_inorder)

#         return new_bst


class Solution2:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Simpler Soln
        Time Complexity: O(n^2) - still not optimal
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root


# optial way to use hashmap so .index is not O(n) and slicing also not O(n) =? O(1) for these operations to make overall O(1)


class Solution3:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Time Complexity: O(n)
        """
        inorder_map = {}
        # for O(1) index lookup
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        def buildTreeHash(
            pi_start: int, pi_end: int, ii_start: int, ii_end: int
        ) -> Optional[TreeNode]:
            """
            Helper fcn to pass index bounds of arr so slicing doesnt take O(n) for each node
            """
            if pi_start > pi_end or ii_start > ii_end:
                return None
            root = TreeNode(preorder[pi_start])
            mid = inorder_map[preorder[pi_start]]
            left_size = mid - ii_start
            root.left = buildTreeHash(
                pi_start + 1, pi_start + left_size, ii_start, mid - 1
            )
            root.right = buildTreeHash(
                pi_start + left_size + 1, pi_end, mid + 1, ii_end
            )
            return root

        return buildTreeHash(0, len(preorder) - 1, 0, len(inorder) - 1)
