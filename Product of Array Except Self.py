class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1]*length

        # prefixsum
        prefix = 1
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]

        print(answer)

        #suffix
        suffix = 1
        for i in range(length -1,-1,-1):
            answer[i] *= suffix 
            suffix *= nums[i]

        return answer
