from collections import Counter 

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        d = Counter(nums)
        for k in d.keys():
            if d[k] == 2:
                result.append(k)
        return result
