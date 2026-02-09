from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0
        c = Counter(chars)

        for word in words:
            good = True
            w = Counter(word)
            for key in w.keys():
                if w[key] > c[key]:
                    good = False
                    break
            if good:
                sum += len(word)

        return sum
