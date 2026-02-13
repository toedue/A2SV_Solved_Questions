class Solution:
    def intToRoman(self, num: int) -> str:
        romans = []
        thousands = num // 1000
        hundreds = (num%1000) // 100
        tens = (num % 100) // 10
        ones = (num) % 10

        roman_thousands = ["", "M", "MM", "MMM"]
        roman_hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        roman_tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        roman_ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return f"{roman_thousands[thousands]}{roman_hundreds[hundreds]}{roman_tens[tens]}{ roman_ones[ones]}"



