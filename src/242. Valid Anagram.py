class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        return Counter(s) == Counter(t)

#############################################

# Alternate Solution without using Counter class
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (len(s) != len(t)):
            return False

        s_count = {}
        t_count = {}

        for character in s:
            s_count[character] = s_count.get(character, 0) + 1

        for character in t:
            t_count[character] = t_count.get(character, 0) + 1

        return s_count == t_count
