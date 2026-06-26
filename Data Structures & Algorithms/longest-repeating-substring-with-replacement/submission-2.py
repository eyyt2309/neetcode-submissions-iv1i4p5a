class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        replacements = 0
        longest = 0
        most_freq = 0
        chars = defaultdict(lambda: 0)

        while r != len(s): # expand right window
            chars[s[r]] += 1
            most_freq = max(most_freq, chars[s[r]])

            if (r - l + 1) - most_freq > k:
                chars[s[l]] -= 1
                l += 1
 

            longest = max(longest, r - l +  1)
            r += 1

        return longest
            

