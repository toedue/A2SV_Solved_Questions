from collections import Counter 

class Solution:
    def findValidPair(self, s: str) -> str:

        d = Counter(s)

        for i in range (1, len(s)):
            if int(s[i-1]) != int(s[i]) and int(s[i-1]) == d[s[i-1]] and int(s[i]) == d[s[i]]:
                return s[i-1] + s[i]
            
        return ""


        
