class SolutionDFS:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        Time Complexity: O(m x n)
        Space: O(mn)
        """
        max_area = 0
        count = 1

        def dfs(r, c, grid) -> int:
            nonlocal count
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for nr, nc in neighbours:
                if self.isValid(nr, nc, grid) and grid[nr][nc] == 1:
                    count += 1
                    dfs(nr, nc, grid)

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if grid[r][c] == 1:
                    count = 1
                    dfs(r, c, grid)
                    max_area = max(max_area, count)
        return max_area
    def isValid(self, r: int, c: int, grid: list[list[int]]):
        return r >= 0 and c >=0 and r < len(grid) and c < len(grid[0])


# class SolutionBFS:
#     def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
#         max_area = 0
#         count = 1
#         queue = deque()
#         for r, row in enumerate(grid):
#             for c, col in enumerate(row):
#                 if grid[r][c] == 1:
#                     count = 1
#                     queue.append((r, c))
#                     grid[r][c] = 0
#                     while queue:
#                         curr_r, curr_c = queue.popleft()
#                         neighbours = [(curr_r + 1, curr_c), (curr_r - 1, curr_c), (curr_r, curr_c + 1), (curr_r, curr_c - 1)]
#                         for nr, nc in neighbours:
#                             if self.isValid(nr, nc, grid) and grid[nr][nc] == 1:
#                                 queue.append((nr, nc))
#                                 grid[nr][nc] = 0
#                                 count += 1
#                     max_area = max(max_area, count)
#         return max_area
#     def isValid(self, r: int, c: int, grid: list[list[int]]):
#         return r >= 0 and c >=0 and r < len(grid) and c < len(grid[0])
    