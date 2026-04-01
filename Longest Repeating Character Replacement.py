from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqTrack = defaultdict(int)

        left = 0
        maxFreq = 0
        maxLength = 0 

        for right in range(len(s)):
            freqTrack[s[right]] += 1
            maxFreq = max(maxFreq,freqTrack[s[right]])

            windowSize = right - left + 1

            if windowSize - maxFreq > k:
                freqTrack[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)


        return maxLength 
            


