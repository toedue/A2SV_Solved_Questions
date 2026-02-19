from collections import Counter

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = Counter()

        for row in responses:
            count.update(set(row))

        return min(count.keys(), key= lambda x: (-count[x],x))
