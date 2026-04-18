class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        for i in range(1, n):
            if nums[i-1] == nums[i]:
                duplicate = nums[i]
            if nums[i] > nums[i-1] + 1:
                missing = nums[i-1] + 1
        if nums[0] != 1:
            missing = 1
        elif nums[-1] != n:
            missing = n

        return [duplicate, missing]
