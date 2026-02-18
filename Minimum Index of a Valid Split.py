from collections import Counter

class Solution:
    def minimumIndex(self, nums: list[int]) -> int:

        d = Counter(nums)
        dominant = max(d, key=d.get)
        total_dominant_count = d[dominant]
        
        # track dominant counts as we move the split point
        left_dominant_count = 0
        n = len(nums)
        
        for i in range(n - 1):
            if nums[i] == dominant:
                left_dominant_count += 1
            
            # count of dominant in the right part
            right_dominant_count = total_dominant_count - left_dominant_count
            
            # lengths of the two parts
            left_len = i + 1
            right_len = n - (i + 1)
            
            # Check the "more than half" condition for both sides
            if left_dominant_count * 2 > left_len and right_dominant_count * 2 > right_len:
                return i
        
        return -1
