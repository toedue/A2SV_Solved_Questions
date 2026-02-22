class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])

        up_ward = True
        res = []

        r,c = 0,0

        while len(res) != row*col:
            if up_ward:
                while r >= 0 and c < col:
                    res.append(mat[r][c])
                    r -= 1
                    c += 1
                if c == col:
                    r +=2
                    c -=1
                else:
                    r += 1
                
                up_ward = False

            else:
                while r < row and c >= 0:
                    res.append(mat[r][c])
                    c -=1
                    r += 1
                    
                if r == row:
                    c += 2
                    r -= 1
                else:
                    c += 1

                up_ward = True
    
        return res
