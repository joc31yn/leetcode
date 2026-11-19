# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str

        Time Complexity: O(n)
        """
        enc = ""

        def enc_preorder(root: Optional[TreeNode]):
            nonlocal enc
            if not root:
                enc += "N,"
                return
            enc += str(root.val) + ","
            enc_preorder(root.left)
            enc_preorder(root.right)

        enc_preorder(root)
        return enc

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode

        Time Complexity: O(n)
        """
        nodes = data.split(",")
        nodes.pop()  # ignore last since encoded ends with ,
        if not nodes:
            return None
        self.index = 0

        def dec_preorder():
            if nodes[self.index] == "N":
                self.index += 1
                return None
            tree = TreeNode(int(nodes[self.index]))
            self.index += 1
            tree.left = dec_preorder()
            tree.right = dec_preorder()
            return tree

        return dec_preorder()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
