class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Time Complexity: O(n) n is length of word
        """
        root = self.root
        for i in range(len(word)):
            if word[i] not in root.children:
                root.children[word[i]] = TrieNode()
            if i == len(word) - 1:
                root.children[word[i]].word_end = True
            root = root.children[word[i]]

    def search(self, word: str) -> bool:
        """
        Time Complexity: O(n) n is length of word
        """
        root = self.root
        i = 0
        while i < len(word) and word[i] in root.children:
            root = root.children[word[i]]
            i += 1
        if i == len(word) and root.word_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Time Complexity: O(n) n is length of prefix
        """
        root = self.root
        i = 0
        while i < len(prefix) and prefix[i] in root.children:
            root = root.children[prefix[i]]
            i += 1
        if i == len(prefix):
            return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
