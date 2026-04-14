class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        map = {0:1}
        count = 0

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        print(nums)

        for i in range(len(nums)):
            if nums[i]%k not in map:
                map[nums[i]%k] = 1
            else:
                count += map[nums[i]%k]
                map[nums[i]%k] += 1

        return count
