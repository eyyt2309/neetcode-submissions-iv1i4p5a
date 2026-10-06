from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()
        words = set(wordList)
        n = len(beginWord)

        queue = deque([(beginWord, 1)])
        visited.add(beginWord)

        while queue:
            currWord, steps = queue.popleft()

            if currWord == endWord:
                return steps

            for nextWord in words:
                for pos in range(n):
                        if nextWord not in visited:
                            if currWord[:pos] == nextWord[:pos] and currWord[pos + 1:] == nextWord[pos + 1:]:
                                visited.add(nextWord)
                                queue.append((nextWord, steps + 1))

        return 0

        
             



