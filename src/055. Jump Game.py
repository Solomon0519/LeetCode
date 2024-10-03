class Solution:
    def canJump(self, nums: List[int]) -> bool:

        end_index = len(nums) - 1

        for prev_step in range(len(nums) - 2, -1, -1):
            if nums[prev_step] < end_index - prev_step:
                continue
            else:
                end_index = prev_step

        return end_index == 0
