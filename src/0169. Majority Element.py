class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority_element = 0
        count = 0

        for i in range(len(nums)):

            current_element = nums[i]

            if (i == 0):
                majority_element = current_element
                count += 1
                continue

            if (current_element == majority_element):
                count += 1
            else:
                count -= 1

            if (count < 0):
                majority_element = nums[i]
                count = 0

        return majority_element
