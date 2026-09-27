class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n, m = len(num1), len(num2)

        # iterate over ch in num1, right to left
        place = 1
        total_1 = 0
        for i in range(n - 1, -1, -1):
            digit = ord(num1[i]) - ord('0')
            total_1 += digit * place
            place *= 10

        # iterate over ch in num2, right to left
        place = 1
        total_2 = 0
        for j in range(m - 1, -1, -1):
            digit = ord(num2[j]) - ord('0')
            total_2 += digit * place
            place *= 10


        return str(total_1 * total_2)
