class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sum = 0
        min_sum = nums[0]

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            # track the min value 
            min_sum = min(min_sum, nums[i])
        # print(nums)
        # print(min_sum)

        return 1 if min_sum > 0 else -min_sum + 1
