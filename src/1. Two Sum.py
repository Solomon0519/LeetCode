class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        remainderDict = {}

        for i in range(len(nums)):
            remainder = target - nums[i]

            if (remainder in remainderDict):
                return [i, remainderDict[remainder]]
            else:
                remainderDict[nums[i]] = i

        return 0