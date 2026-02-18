from collections import Counter 

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        frq_s = Counter(s)
        frq_t = Counter(t)

        if frq_s == frq_t:
            return 0

        step = 0

        for key in frq_t.keys():
            if key in frq_s.keys():
                step += min(frq_s[key], frq_t[key])

        return len(s)- step
