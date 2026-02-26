class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        size = len(nums)
        for i, num in enumerate(nums):
            nums[i] = str(num)
        

        #bubble sort
        for i in range (size):
            for j in range(0, size - 1 - i):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        result = "".join(nums)

        if result[0] == '0':
            return "0"

        return result

