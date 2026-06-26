class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isWord = False

    def __init__(self):
        self.tree = self.TrieNode()

    def addWord(self, word: str) -> None:
        node = self.tree
        for ch in word:
            if ch not in node.children:
                node.children[ch] = self.TrieNode()
            node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        n = len(word)

        def dfs(word, pos, node):
            if pos == n:
                return node.isWord
            found = False
            if word[pos] == '.': # if current char is . check all children of current treenode
                for child in node.children:
                    found = found or dfs(word, pos + 1, node.children[child])
            elif word[pos] in node.children: # if current char in node children, traverse node
                found = found or dfs(word, pos + 1, node.children[word[pos]])
            
            return found

        if not word:
            return False
        node = self.tree
        return dfs(word, 0, node)
