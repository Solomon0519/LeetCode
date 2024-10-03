class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        dimension = len(matrix[0])

        for i in range(dimension):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        print(matrix)

        for i in range(dimension):
            matrix[i], matrix[dimension - i - 1] = matrix[dimension - i - 1], matrix[i]