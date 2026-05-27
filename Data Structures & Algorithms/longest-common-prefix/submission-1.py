class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.isWord = False

    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        def append(node, s):
            for ch in s:
                if ch not in node.children:
                    node.children[ch] = Solution.TrieNode()
                node = node.children[ch]
            node.isWord = True

        node = Solution.TrieNode()
        for s in strs:
            append(node, s)
        prefix = 0
        print(node.children)
        for ch in strs[0]:
            if ch in node.children and len(node.children) == 1:
                node = node.children[ch]
                prefix += 1

        return strs[0][:prefix]