class Solution:
    def isValid(self, row: int, col: int, board: List[List[str]]):
        if row >= 0 and col >= 0 and row < len(board) and col < len(board[0]):
            return True
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time Complexity: O(m * 4^n), m is number cells in board, n is length of word
        """
        visited = [([False] * len(board[0])) for _ in range(len(board))]

        def dfs(i: int, word: str, board: List[List[str]], row: int, col: int):
            if i == len(word):
                return True
            visited[row][col] = True
            neighbours = [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]
            for r, c in neighbours:
                if (
                    self.isValid(r, c, board)
                    and not visited[r][c]
                    and board[r][c] == word[i]
                ):
                    found = dfs(i + 1, word, board, r, c)
                    if found:
                        return True
                    else:
                        visited[r][c] = False
            return False

        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if word[0] == c:
                    found = dfs(1, word, board, i, j)
                    if found:
                        return True
                    visited = [([False] * len(board[0])) for _ in range(len(board))]
        return False
