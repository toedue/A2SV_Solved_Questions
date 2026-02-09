from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        frq = Counter(nums)

        for key in frq.keys():
            if frq[key] == 1:
                return key
