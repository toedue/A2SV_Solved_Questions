class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        row = len(matrix)
        col = len(matrix[0])
        copy = [row[:] for row in matrix]

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:

                    # set entire row to 0
                    for r in range(row):
                        copy[r][j] = 0

                    # set entire column to 0
                    for c in range(col):
                        copy[i][c] = 0

        for i in range(row):
            for j in range(col):
                matrix[i][j] = copy[i][j]


        
