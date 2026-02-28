from collections import Counter 

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        d = Counter(s)
        result = []

        for char in order:
            if char in d:
                result.append(char*d[char])
                del d[char]

        for key, value in d.items():
            result.append(key * value)

        return "".join(result)
