class PrefixTree:

    def __init__(self):
        self.rootNode = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.rootNode

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TreeNode(ch)
            curr = curr.children[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        
        curr = self.rootNode

        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.rootNode

        for ch in prefix:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return True
        
class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.isEnd = False