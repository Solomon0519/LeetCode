class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1_to_int = 0
        num2_to_int = 0

        for i in num1:
            num1_to_int = num1_to_int * 10 + (ord(i) - 48)

        for j in num2:
            num2_to_int = num2_to_int * 10 + (ord(j) - 48)

        return str(num1_to_int * num2_to_int)