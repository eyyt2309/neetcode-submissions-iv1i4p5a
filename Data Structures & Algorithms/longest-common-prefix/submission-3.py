class Solution:
    class TrieNode():
        def __init__(self) -> None:
            self.children = {}
            self.isWord = False
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def insertString(s, trie):
            for ch in s:
                if ch not in trie.children:
                    trie.children[ch] = Solution.TrieNode()
                trie = trie.children[ch]
            trie.isWord = True
        root = Solution.TrieNode()
        for s in strs:
            insertString(s, root)
        
        trie = root
        ans = ""
        for ch in strs[0]:
            if len(trie.children) == 1 and trie.isWord == False:
                trie = trie.children[ch]
                ans += ch
        return ans
        