class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix: 
            return []
        
        row_begin = 0
        row_end = len(matrix) -1
        col_begin = 0
        col_end = len(matrix[0])-1

        result = []


        while row_begin <= row_end and col_begin <= col_end:

            #traverse right 
            for j in range(col_begin, col_end + 1):
                result.append(matrix[row_begin][j])
            row_begin += 1

            #traverse down
            for j in range(row_begin, row_end + 1):
                result.append(matrix[j][col_end])
            col_end -= 1

            #traverse left
            if row_begin <= row_end:
                for j in range(col_end, col_begin -1, -1):
                    result.append(matrix[row_end][j])
                row_end -= 1

            # traverse up
            if col_begin <= col_end:
                for i in range(row_end, row_begin -1, -1):
                    result.append(matrix[i][col_begin])
                col_begin += 1

            
        return result

