def next_no(n):
        result = 0
        while n: #true
            #takes the last digit
            digit = n% 10
            result += digit **2
            # the remaning digits
            n //= 10 # update n
        return result

class Solution:
    def isHappy(self, n: int) -> bool:
        set_ = set()

        while n not in set_:
            set_.add(n)
            n = next_no(n)
            if n == 1:
                return True
        return False
