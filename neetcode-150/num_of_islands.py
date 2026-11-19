class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Time Complexity: O(m * n) where m, n are dimensions of grid
        """
        count = 0
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def bfs(r: int, c: int):
            neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            visited[r][c] = True
            for row, col in neighbours:
                if (
                    self.isValid(row, col, grid)
                    and not visited[row][col]
                    and grid[row][col] == "1"
                ):
                    bfs(row, col)

        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if not visited[i][j] and grid[i][j] == "1":
                    bfs(i, j)
                    count += 1
        return count

    def isValid(self, r: int, c: int, grid: List[List[str]]) -> bool:
        """
        Time Complexity: O(1)
        """
        if r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]):
            return True
        return False
