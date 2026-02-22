class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row, column = len(img), len(img[0])
        res = [[0]*column for _ in range(row)]

        for r in range(row):
            for c in range(column):
                total, count = 0,0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if i<0 or i==row or j < 0 or j == column:
                            continue
                        total += img[i][j]
                        count +=1

                temp = total // count 

                res[r][c] = temp
        return res
