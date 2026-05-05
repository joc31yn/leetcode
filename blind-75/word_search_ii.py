class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False
        self.index = -1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Time Complexity: O(m * n * 4 * 3^(t - 1) + s)
        m: # rows, n: # cols, t: length of longest word, s: sum of length of all words
        m * n : each sell as starting point of search
        4 * 3^(t - 1) : recursive call, first cell could have 4 possible branchings,
        each subsequent only has 3 possible branchings since cannot go back to prev
        s: time complexity to build trie
        """
        root = TrieNode()
        for i, w in enumerate(words):
            self.insertWord(root, w, i)
        sol = []
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(board: List[List[int]], r: int, c: int, root: TrieNode):
            if root.word_end and root.index >= 0:
                sol.append(words[root.index])
                root.index = -1  # ensure no duplicates
            visited[r][c] = True
            neighbours = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            for row, col in neighbours:
                if (
                    self.isValid(row, col, board)
                    and not visited[row][col]
                    and board[row][col] in root.children
                ):
                    dfs(board, row, col, root.children[board[row][col]])
                    visited[row][col] = False

        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c in root.children:
                    dfs(board, i, j, root.children[c])
                    visited = [[False] * len(board[0]) for _ in range(len(board))]
        return sol

    def isValid(self, r: int, c: int, board: [list[List[int]]]):
        """
        Time Complexity: O(1)
        """
        if r >= 0 and c >= 0 and r < len(board) and c < len(board[0]):
            return True
        return False

    def insertWord(self, root: TrieNode, word: str, i: int):
        """
        Time Complexity: O(s) where s is length of word
        """
        curr = root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.word_end = True
        curr.index = i
