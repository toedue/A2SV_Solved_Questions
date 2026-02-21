from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        d_c1 = Counter(word1)
        d_c2 = Counter(word2)

        return d_c1.keys() == d_c2.keys() and sorted(d_c1.values()) == sorted(d_c2.values())
