class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        target_pixel_color = image[sr][sc]

        if color == target_pixel_color:
            return image

        m = len(image)
        n = len(image[0])

        def depth_first_search(row: int, column: int) -> None:
            if (row < 0) or (row >= m):
                return
            if (column < 0) or (column >= n):
                return
            if (image[row][column] != target_pixel_color):
                return

            image[row][column] = color
            depth_first_search(row - 1, column)
            depth_first_search(row + 1, column)
            depth_first_search(row, column - 1)
            depth_first_search(row, column + 1)

        depth_first_search(sr, sc)

        return image