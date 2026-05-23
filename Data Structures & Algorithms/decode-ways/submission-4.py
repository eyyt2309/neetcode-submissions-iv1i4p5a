class Solution:
    def numDecodings(self, s: str) -> int:
        chars = {
            str(i + 1): chr(ord('A') + i)
            for i in range(26)
        }
        memo = {}

        def dfs(new_str):
            if len(new_str) == 0:
                return 1
            if new_str[0] == "0":
                return 0
            if new_str in memo:
                return memo[new_str]

            ways = 0
            for char in chars:
                char_len = len(char)
                if new_str[0:0 + char_len] == char:
                    ways += dfs(new_str[char_len:])
            
            memo[new_str] = ways
            return ways
        
        return dfs(s)