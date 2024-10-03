class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        modulo_dictionary = {}
        for num in arr:
            num %= k
            modulo_dictionary[num] = modulo_dictionary.get(num, 0) + 1

        print(modulo_dictionary)

        if (modulo_dictionary.get(0, 0) % 2 != 0):
            return False

        for i in range(1, (k // 2) + 1):
            if (modulo_dictionary.get(i, 0) - modulo_dictionary.get(k - i, 0) != 0):
                return False

        return True