class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        row = len(mat)
        col= len(mat[0])

        if mat == target:
                return True
        temp = [[0]*col for _ in range(row)]
        # first rotation
        for i in range(row):
            for j in range(col):
                temp[j][col-i-1] = mat[i][j]

        if temp == target:
            return True
        
        mat = temp
        
        temp = [[0]*col for _ in range(row)]
        # second rotation
        for i in range(row):
            for j in range(col):
                temp[j][col-i-1] = mat[i][j]

        if temp == target:
            return True
        
        mat = temp

        temp = [[0]*col for _ in range(row)]
        # third rotation
        for i in range(row):
            for j in range(col):
                temp[j][col-i-1] = mat[i][j]

        if temp == target:
            return True

        return False



