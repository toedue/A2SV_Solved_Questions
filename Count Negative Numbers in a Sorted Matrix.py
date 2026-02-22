class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        counter = 0
        for row in grid:
            for i in range(len(row)-1, -1, -1):
                if row[i] >=0:
                    break
                else:
                    counter +=1
                    
        return counter



