class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def isPalindrome(s):
            n = len(s)
            if n == 1:
                return True
            l, r = 0, n - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True   

        def dfs(arr, s):
            # if remaining string empty, append arr to ans
            if len(s) == 0:
                ans.append(arr.copy())
                return

            for i in range(1, len(s) + 1):
                new_s = s[:i]
                if isPalindrome(new_s):
                    arr.append(new_s)
                    dfs(arr, s[i:])
                    arr.pop()
        arr = []
        dfs(arr, s)
        return ans