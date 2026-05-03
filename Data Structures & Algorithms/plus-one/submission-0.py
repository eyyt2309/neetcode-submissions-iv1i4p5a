class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 0
        ans = []
        
        for i, num in enumerate(reversed(digits)):
            total = num + carry
            carry = 0
            if i == 0:
                total += 1

            if total > 9:
                total = total - 10
                carry = 1

            ans.insert(0, total)
        
        if carry != 0:
            ans.insert(0, carry)

        return ans