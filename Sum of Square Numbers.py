class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(c-1):
            if (i*i) + ((i +1)*(i + 1)) == c:
                return True
        return False
        
