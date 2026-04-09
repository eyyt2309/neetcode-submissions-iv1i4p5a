class Solution:
    def myPow(self, x: float, n: int) -> float:

        power = x
        
        if n == 0:
            return 1

        if n > 0:
            for i in range(n - 1):
                x = x * power
            return x
        else:
            for i in range(-(n) - 1):
                x = x * power
            return (1 / x)