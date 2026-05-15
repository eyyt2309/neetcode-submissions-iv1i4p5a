class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def recurPalindrome(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    recurPalindrome(j+1)
                    part.pop()

        recurPalindrome(0)
        return res



        


@staticmethod
def isPalindrome(s):
    if len(s) == 0:
        return False
    if len(s) == 1:
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True