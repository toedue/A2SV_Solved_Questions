from collections import Counter 

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) == 1 or len(changed) == 0 or len(changed) % 2 == 1:
            return []

        orginal = []
        half = len(changed)//2

        freq = Counter(changed)

        if freq[0]%2 == 1:
            return []

        for num in sorted(freq.keys()):
            while(freq[num] > 0):
                if freq[2*num] <= 0:
                    return []
                else: # the pair exist
                    orginal.append(num)
                    freq[num] -= 1
                    freq[2*num] -=1
                    if len(orginal) == half:
                        return orginal


        
