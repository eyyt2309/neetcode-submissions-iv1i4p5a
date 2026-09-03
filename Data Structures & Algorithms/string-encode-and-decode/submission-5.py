class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            n = len(s)
            new_s = str(n) + '#'  + s
            result += new_s

        return result

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        n = len(s)

        start = 0
        result = []

        while True:
            end = start
            while s[end] != '#':
                end += 1
            s_len = int(s[start: end])

            new_s = s[end + 1: end + 1 + s_len]
            result.append(new_s)

            start = end + 1 + s_len
            if start == n:
                break

        return result