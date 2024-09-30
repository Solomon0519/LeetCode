class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix_dict = {}
        prefix_score_sum = []

        for word in words:
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                if prefix in prefix_dict:
                    prefix_dict[prefix] += 1
                else:
                    prefix_dict[prefix] = 1

        for word in words:
            score = 0
            for i in range(1, len(word) + 1):
                prefix = word[:i]
                score += prefix_dict[prefix]
            prefix_score_sum.append(score)

        return prefix_score_sum