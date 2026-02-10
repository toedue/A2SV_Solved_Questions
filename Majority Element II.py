from collections import Counter 

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        d = Counter(nums)

        return [x for x in d.keys() if d[x] > n//3]
        
