from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        l, r = 0, 0
        max_char = 0
        ans = 0

        while r < len(s):
            char_count[s[r]] = char_count.get(s[r], 0) + 1

            max_char = max(char_count[s[r]], max_char)
            replacements = r - l + 1 - max_char

            if replacements > k:
                char_count[s[l]] -= 1
                l += 1

            ans = max(r-l + 1, ans)
            r += 1

        return ans



        

        