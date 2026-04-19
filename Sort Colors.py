class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        buckets = [0,0,0]

        for i in range(len(nums)):
            buckets[nums[i]] += 1

        print(buckets)

        i = 0
        for color in range(3):
            for _ in range(buckets[color]):
                nums[i] = color
                i += 1
