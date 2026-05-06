class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(m * n) where m, n are dimensions of heights
        """
        sol = []
        pacific_cells = set()
        atlantic_cells = set()

        def dfs(r: int, c: int, heights: List[List[int]], visited: set):
            visited.add((r, c))
            neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for row, col in neighbours:
                if (
                    self.isValid(row, col, heights)
                    and heights[row][col] >= heights[r][c]
                    and (row, col) not in visited
                ):
                    dfs(row, col, heights, visited)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                cell = (i, j)
                if self.isPacific(i, j):
                    pacific_cells.add(cell)
                    dfs(i, j, heights, pacific_cells)
                if self.isAtlantic(i, j, heights):
                    atlantic_cells.add(cell)
                    dfs(i, j, heights, atlantic_cells)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i, j) in pacific_cells and (i, j) in atlantic_cells:
                    sol.append([i, j])
        return sol

    def isValid(self, r: int, c: int, heights: List[List[int]]) -> bool:
        if r >= 0 and c >= 0 and r < len(heights) and c < len(heights[0]):
            return True
        return False

    def isPacific(self, r: int, c: int) -> bool:
        if min(r, c) == 0:
            return True
        return False

    def isAtlantic(self, r: int, c: int, heights: List[List[int]]) -> bool:
        if r == len(heights) - 1 or c == len(heights[0]) - 1:
            return True
        return False


# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         sol = []
#         visited = [[False] * len(heights[0]) for _ in range(len(heights))]
#         possible_cells = set()

#         def dfs(r: int, c: int, heights: List[List[int]]):
#             nonlocal pacific, atlantic
#             if (r, c) in possible_cells:
#                 return True
#             if self.isPacific(r, c, heights):
#                 pacific = True
#             if self.isAtlantic(r, c, heights):
#                 atlantic = True
#             if pacific and atlantic:
#                 return True
#             visited[r][c] = True
#             neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
#             for row, col in neighbours:
#                 if (
#                     self.isValid(row, col, heights)
#                     and not visited[row][col]
#                     and heights[row][col] <= heights[r][c]
#                 ):
#                     found = dfs(row, col, heights)
#                     if found:
#                         return True
#             return False

#         for i, row in enumerate(heights):
#             for j, c in enumerate(row):
#                 pacific = False
#                 atlantic = False
#                 if dfs(i, j, heights):
#                     sol.append([i, j])
#                     possible_cells.add((i, j))
#                 visited = [[False] * len(heights[0]) for _ in range(len(heights))]

#         return sol

#     def isValid(self, r: int, c: int, heights: List[List[int]]) -> bool:
#         if r >= 0 and c >= 0 and r < len(heights) and c < len(heights[0]):
#             return True
#         return False

#     def isPacific(self, r: int, c: int, heights: List[List[int]]) -> bool:
#         if min(r, c) == 0:
#             return True
#         return False

#     def isAtlantic(self, r: int, c: int, heights: List[List[int]]) -> bool:
#         if c == len(heights[0]) - 1 or r == len(heights) - 1:
#             return True
#         return False
