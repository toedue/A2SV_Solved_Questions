class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        dict= {}
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in dict:
                dict[sorted_nums[i]] = i
        for i in nums:
            res.append(dict[i])
        return res


        

