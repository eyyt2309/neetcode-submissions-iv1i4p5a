class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        hashmap = {}
        hashmap['2'] = ['a','b','c']
        hashmap['3'] = ['d','e','f']
        hashmap['4'] = ['g','h','i']
        hashmap['5'] = ['j','k','l']
        hashmap['6'] = ['m','n','o']
        hashmap['7'] = ['p','q','r','s']
        hashmap['8'] = ['t','u','v']
        hashmap['9'] = ['w','x','y','z']
        ans = []

        def dfs(digits, idx, s):
            if idx == len(digits):
                ans.append(s)
                return
            for ch in hashmap[digits[idx]]:
                dfs(digits, idx + 1, s + ch)

            return

        dfs(digits, 0, "")
        return ans

