class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {"I":1,"V":5,"X":10, "L":50, "C":100,"D":500,"M":1000}
        result = 0
        for i in range(len(s) - 1): 
            if dict_[s[i]] < dict_[s[i+1]]:
                result -= dict_[s[i]]
            else: #dict_[s[i]] < dict_[s[i+1]] and #dict_[s[i]] = dict_[s[i+1]]
                result += dict_[s[i]]

        result += dict_[s[-1]] # add the last one
        return result
