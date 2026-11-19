class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Time Complexity: O(V + E)
        """
        graph = {}
        for i in range(n):
            graph[i] = []
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        visited = set()  # which nodes you can reach
        seen = set()  # nodes seen in a path

        # checks for cycles and tracks which nodes can be reached
        def dfs(start: int, prev: int):
            if start in seen:
                return False
            seen.add(start)
            if start not in visited:
                visited.add(start)
            for n in graph[start]:
                if n != prev and not dfs(n, start):
                    return False
            seen.remove(start)
            return True

        # if no cycles and all nodes were visited (meaning connected) => valid tree
        return dfs(0, -1) and len(visited) == n
