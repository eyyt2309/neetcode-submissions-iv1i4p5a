from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        left = 0 

        ch = Counter(t)
        window = {}

        have = 0
        need_count = len(ch)

        res = [-1,-1]
        res_len = float('inf')



        for right in range(len(s)):
            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in ch and window[char] == ch[char]:
                have += 1

            while have == need_count:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = (right - left + 1)

                # try to reduce left side of window
                window[s[left]] -= 1
                if s[left] in ch and window[s[left]] < ch[s[left]]:
                    have -= 1
                
                left += 1

        left, right = res

        return s[left:right + 1] if res_len != float('inf') else ""

