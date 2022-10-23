class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for item in matrix:
            l = 0
            r = len(matrix[0])-1
            while l < r:
                item[l], item[r] = item[r], item[l]
                l += 1
                r -= 1

        return matrix