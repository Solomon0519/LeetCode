class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x

        value = 1
        product = x
        n = abs(n)

        while n > 0:
            if n % 2 == 1:
                value *= product
            product *= product
            n //= 2

        return value