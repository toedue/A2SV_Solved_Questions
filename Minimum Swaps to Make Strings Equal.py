from collections import Counter
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        frq = Counter(s1 + s2)
        #if they are odd we cant swap

        if frq['x'] % 2 == 1 or frq['y'] == 1:
            return -1

        d = defaultdict(int)

        for i, j in zip(s1, s2):
            if i != j:
                d[i+j] += 1

        res = 0

        for val in d.values():
            if val % 2 == 0:
                res += val//2

            elif val % 2 == 1:
                res += val//2 + 1

        return res
        
