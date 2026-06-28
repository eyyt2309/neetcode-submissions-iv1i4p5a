class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        ans = []
        if not digits:
            return []
        digit_map = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        def dfs(pos, s):
            if pos == len(digits):
                ans.append(s)
                return
            
            for ch in digit_map[digits[pos]]:
                new_string = s + ch
                dfs(pos + 1, new_string)

        dfs(0, "")

        return ans