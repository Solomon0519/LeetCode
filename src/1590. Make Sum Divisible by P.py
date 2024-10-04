class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        nums_sum = sum(nums) #O(N)

        if nums_sum % p == 0:
            return 0

        remainder = nums_sum % p
        prefix_sum = 0
        prefix_sum_array = {0: -1}
        minimum_subarray_length = float('inf')

        for index, num in enumerate(nums):
            prefix_sum += num
            current_remainder = prefix_sum % p
            value = (prefix_sum - remainder) % p


            if value in prefix_sum_array:
                minimum_subarray_length = min(minimum_subarray_length, index - prefix_sum_array[value])

            prefix_sum_array[current_remainder] = index

        if minimum_subarray_length == float('inf'):
            return -1
        elif (minimum_subarray_length == len(nums)):
            return -1
        else:
            return minimum_subarray_length