class Solution:
    def longestPalindrome(self, s: str) -> int:

        string_length = len(s)

        if (string_length <= 1):
            return string_length

        else:
            string_character_counter = Counter(s)
            max_string_length = 0
            max_odd = 0

            for character in string_character_counter:
                occurence = string_character_counter[character]
                if (occurence % 2 == 1):
                    if (occurence >= max_odd):
                        if (max_odd == 0):
                            max_odd = occurence
                            continue
                        max_string_length += (max_odd - 1)
                        max_odd = occurence
                    else:
                        max_string_length += occurence - 1
                else:
                    max_string_length += occurence

            return max_string_length + max_odd