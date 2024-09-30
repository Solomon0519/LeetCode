class Solution:
    def reverse(self, x: int) -> int:

        min_value = -2**31
        max_value = 2**31 - 1

        reverse_x_string = str(abs(x))[::-1]
        reverse_x_int = int(reverse_x_string)

        if x < 0:
            reverse_x_int *= -1

        if reverse_x_int < min_value or reverse_x_int > max_value:
            return 0

        return reverse_x_int