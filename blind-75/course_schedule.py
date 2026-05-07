class Solution:
    """
    More efficient sol w similar idea to Solution3
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Time Complexity: O(V + E) where V is number of courses and E number of prereq pairs
        """
        prereqs = {}
        for course, pre in prerequisites:
            if course not in prereqs:
                prereqs[course] = [pre]
            else:
                prereqs[course].append(pre)
        for i in range(numCourses):
            if i not in prereqs:
                prereqs[i] = []

        seen = set()

        def dfs(node: int):
            if node in seen:
                return False
            if not prereqs[node]:
                return True
            seen.add(node)
            for p in prereqs[node]:
                if not dfs(p):
                    return False
            seen.remove(node)
            prereqs[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


# class Solution2:
#     """
#     Mathematical way using bfs to see if a topological sort exsits
#     """
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         prereqs = {}
#         incoming = {}
#         for p in prerequisites:
#             if p[0] not in prereqs:
#                 prereqs[p[0]] = [p[1]]
#             else:
#                 prereqs[p[0]].append(p[1])
#             if p[1] not in incoming:
#                 incoming[p[1]] = {p[0]}
#             else:
#                 incoming[p[1]].add(p[0])
#         s = [] # courses w no prereqs (i.e. no incoming edges)
#         graph = {}
#         # construct graph
#         for i in range(numCourses):
#             if i not in incoming:
#                 s.append(i)
#             if i not in prereqs:
#                 graph[i] = Node(i)
#             else:
#                 graph[i] = Node(i, prereqs[i])
#         while s:
#             node = graph[s.pop()]
#             for i in range(len(node.neighbours) - 1, -1, -1):
#                 nei = node.neighbours.pop()
#                 if nei in incoming:
#                     incoming[nei].remove(node.val)
#                     if len(incoming[nei]) == 0:
#                         s.append(nei)
#         for v in incoming.values():
#             if len(v) > 0:
#                 return False
#         return True


# class Node:
#     def __init__(self, val=-1, neighbours=[]):
#         self.val = val
#         self.neighbours = neighbours

# class Solution3:
#     """
#     Too Slow, TLE
#     """
#     def isCycle(self, start: int, graph: dict[int, Node]):
#         seen = set()

#         def dfs(n: Node):
#             if n.val in seen:
#                 return True
#             seen.add(n.val)
#             for nei in n.neighbours:
#                 if dfs(graph[nei]):
#                     return True
#                 seen.remove(nei)
#             return False

#         return dfs(graph[start])

#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # if there is cycle, not possible
#         prereqs = {}
#         for p in prerequisites:
#             if p[0] not in prereqs:
#                 prereqs[p[0]] = [p[1]]
#             else:
#                 prereqs[p[0]].append(p[1])
#         # create graph with hashable keys
#         graph = {}
#         for i in range(numCourses):
#             if i not in prereqs:
#                 graph[i] = Node(i)
#             else:
#                 graph[i] = Node(i, prereqs[i])
#         for key in graph.keys():
#             if self.isCycle(key, graph):
#                 return False
#         return True
