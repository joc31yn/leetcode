class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Time Complexity: O(n)
        """
        root = self.root
        for c in word:
            if c not in root.children:
                root.children[c] = TrieNode()
            root = root.children[c]
        root.word_end = True

    def search(self, word: str) -> bool:
        """
        Time Complexity: O(26^2 * (n-2)) => O(n)
        Since given constraint is at most 2 .
        """

        def dfs(root: TrieNode, i: int) -> bool:
            if i == len(word) and root.word_end:
                return True
            if i >= len(word):
                return False
            if word[i] == ".":
                for _, val in root.children.items():
                    if dfs(val, i + 1):
                        return True
                return False
            if word[i] not in root.children:
                return False
            root = root.children[word[i]]
            return dfs(root, i + 1)

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
