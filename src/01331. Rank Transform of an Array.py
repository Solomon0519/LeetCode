class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        unique_array = sorted(set(arr))
        rank_dict  = {}

        for rank, value in enumerate(unique_array):
            rank_dict[value] = rank + 1

        return [rank_dict[element] for element in arr]