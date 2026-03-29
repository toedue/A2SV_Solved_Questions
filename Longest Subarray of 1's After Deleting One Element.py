class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        max_length = 0
        start = 0
        zero_position = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                start = zero_position + 1
                zero_position = i

            max_length = max(max_length, i-start)

        return max_length
        
