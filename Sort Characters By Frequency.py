from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:

        count = Counter(s)
        result = ""

        sort = sorted(count.keys(), key= lambda x: (-count[x]))

        for char in sort:
            result += char * count[char]


        return result
