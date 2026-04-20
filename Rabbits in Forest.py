from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total = 0

        for i in freq.keys():
            group_size = i + 1

            groups = math.ceil(freq[i]/group_size)

            total += groups * group_size

        return total
