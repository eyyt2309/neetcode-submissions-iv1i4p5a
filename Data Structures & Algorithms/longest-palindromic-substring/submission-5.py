class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        if len(s) == 1:
            return s
        palindrome = ""

        def expand(left, right, s):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for idx in range(len(s)):
            odd = expand(idx, idx, s)
            even = expand(idx, idx + 1, s)

            if len(odd) > longest:
                longest = len(odd)
                palindrome = odd
            if len(even) > longest:
                longest = len(even)
                palindrome = even

        
        return palindrome