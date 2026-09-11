from functools import cache

class Solution:
    class TrieNode:
        def __init__(self, char = None):
            self.children = {}
            self.word = None

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        tree = Solution.TrieNode()
        def addWord(word, node):
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Solution.TrieNode()
                node = node.children[ch]
            node.word = word
        for word in dictionary:
            addWord(word, tree)
        n = len(s)

        @cache
        def dfs(idx):
            if idx >= n:
                return 0

            # Option 1: treat s[idx] as an extra character
            least = 1 + dfs(idx + 1)

            # Option 2: try matching dictionary words starting at idx
            if s[idx] not in tree.children:
                return least

            node = tree.children[s[idx]]
            curr = idx

            while True:
                if node.word is not None:
                    least = min(
                        least,
                        dfs(curr + 1)
                    )

                curr += 1

                if curr >= n or s[curr] not in node.children:
                    break

                node = node.children[s[curr]]

            return least


        return dfs(0)

