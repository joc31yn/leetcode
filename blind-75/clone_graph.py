# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Time Complexity: O(V + E)
        """
        seen = {}

        def dfs(node: Optional["Node"]):
            if not node:
                return None
            if node in seen:
                return seen[node]
            clone = Node(node.val)
            seen[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone

        return dfs(node)


# Alt Solution, more intuitive, but more code
# from typing import Optional
# class Solution2:
#     def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
#         """
#         Time Complexity: O(V + 2E) => O(V + E)
#         """
#         cloned = {}
#         # copy all nodes w/o neighbours
#         def clone(node: Optional['Node']):
#             if not node or node in cloned:
#                 return
#             copy = Node(node.val)
#             cloned[node] = copy
#             for n in node.neighbors:
#                 clone(n)
#         clone(node)
#         seen = set() # ensures we dont get in infinite loop
#         # link all node copies (i.e. add neighbours)
#         def dfs(node):
#             if not node:
#                 return None
#             seen.add(node)
#             for n in node.neighbors:
#                 cloned[node].neighbors.append(cloned[n])
#                 if n not in seen:
#                     dfs(n)
#             return cloned[node]
#         return dfs(node)
