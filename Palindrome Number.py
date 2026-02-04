class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if thr number is negative it cant be a palindrome
        # if a number ends with zero, cant be a palindrome
        if (x % 10 == 0 and x != 0) or (x < 0):
            return False 

        # reverse the number to check the palindrome
        reverse_x = 0
        
        while reverse_x < x:
            reverse_x = reverse_x*10 + x%10
            x //= 10

        return reverse_x == x or reverse_x//10 == x
