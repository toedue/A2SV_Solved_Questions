class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        sett = set()
        sett2 = set()
        for num in nums1:
            if num not in sett:
                sett.add(num)
        for num in nums2:
            if num in sett:
                sett2.add(num)
        final = list(sett2)
        return final
        
