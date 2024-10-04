class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort() # O(nlogn)
        target_level = skill[0] + skill[-1]
        chemistry_level = skill[0] * skill[-1]
        left, right = 1, len(skill) - 2

        while (left < right):
            level_sum = skill[left] + skill[right]
            if (level_sum != target_level):
                return -1
            else:
                chemistry_level += (skill[left] * skill[right])
                left += 1
                right -= 1

        return chemistry_level