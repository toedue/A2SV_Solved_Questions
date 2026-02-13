class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        # sort  the list of nums 
        nums.sort()
        
        longest = 1
        current = 1

        for i in range(1, len(nums)):
            # ignore dublicates
            if nums[i] == nums[i - 1]:
                continue 
            elif nums[i-1] + 1 == nums[i]:
                current += 1
            else: # nums[i] is not a duplicate and a consecutive
                longest = max(longest, current)
                current = 1
            

        return max(longest, current)
