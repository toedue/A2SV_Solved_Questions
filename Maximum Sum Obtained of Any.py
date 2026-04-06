class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        frequency = [0]*len(nums)

        for start , end in requests:
            frequency[start] += 1
            if end + 1 < len(nums):
                frequency[end + 1] -= 1

        # prefixsum

        for i in range(1, len(frequency)):
            frequency[i] += frequency[i-1]

        print(frequency)

        total = 0
        nums.sort()
        frequency.sort()

        print(frequency)
        print(nums)


        for i in range(len(nums)):
            total += (frequency[i] * nums[i])


        return total % (10**9 + 7)

  
