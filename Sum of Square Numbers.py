import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        c_sqrt= math.sqrt(c)


        for a in range(int(c_sqrt) + 1):
            b = c - a*a
            b2 = int(math.sqrt(b))
            if b2*b2 == b:
                return True

        return False
        
