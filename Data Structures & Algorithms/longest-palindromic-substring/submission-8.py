class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = float('-inf')
        substring = [None, None]

        n = len(s)

        for i in range(n):

            # odd length palindrome
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1> longest:
                    longest = r - l + 1
                    substring = [l, r]
                l -= 1
                r += 1

            # even length palindrome
            l, r = i - 1, i

            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1> longest:
                    longest = r - l + 1
                    substring = [l, r]
                l -= 1
                r += 1

        return s[substring[0]:substring[1] + 1]


            