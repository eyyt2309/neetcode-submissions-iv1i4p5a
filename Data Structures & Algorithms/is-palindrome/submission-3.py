class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        strlen = len(s)

        left = 0
        right = strlen - 1

        while left < right:
            print("Left: {0}".format(s[left].lower()))
            print("Right: {0}".format(s[right].lower()))
            
            if s[left].isalnum() == False:
                left += 1
            elif s[right].isalnum() == False:
                right -= 1 
            elif s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True


            