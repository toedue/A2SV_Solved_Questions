class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
        remainders = []

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        for i in range(len(nums)):
            remainders.append(nums[i]%k)

        # print(remainders)

        for idx, val in enumerate(remainders):
            if val in d:
                if idx - d[val] >= 2:
                    return True 
            else:
                d[val]=idx
                

        return  False
