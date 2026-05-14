from collections import Counter
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        chars = Counter(s1 + s2)
        target_chars = Counter(s3)
        length = len(s1 + s2)

        if chars != target_chars:
            return False
        if len(s1) == 0 and len(s2) == 0 and len(s3) == 0:
            return True
    
        memo = {}
        self.recurString(s1, s2, s3, 0, 0, length, memo)

        print(memo)

        return memo[(0, 0)]


    def recurString(self, s1, s2, s3, i, j, strlen, memo):
        if i + j >= strlen:
            return True
        if (i,j) in memo:
            return memo[(i,j)]

        memo[(i, j)] = False

        if i < len(s1) and s1[i] == s3[i + j]:
            memo[(i, j)] = False or self.recurString(s1, s2, s3, i + 1, j, strlen, memo)
        if j < len(s2) and s2[j] == s3[i + j]:
            memo[(i, j)] = False or self.recurString(s1, s2, s3, i, j + 1, strlen, memo)

        return memo[(i, j)]
