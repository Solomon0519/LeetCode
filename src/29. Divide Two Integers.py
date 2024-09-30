class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        min_value = -2 ** 31
        max_value = 2 ** 31 - 1

        if dividend == min_value and divisor == -1:
            return max_value

        negative = (dividend < 0) ^ (divisor < 0)

        dividend_abs = abs(dividend)
        divisor_abs = abs(divisor)

        quotient = 0

        for i in range(31, -1, -1):
            if (dividend_abs >> i) >= divisor_abs:
                quotient += 1 << i
                dividend_abs -= divisor_abs << i

        if negative:
            quotient = -quotient

        return max(min(quotient, max_value), min_value)