class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mini = nums[0]

        for num in nums:
            while( stack and num >= stack[-1][0]):
                stack.pop()

            if stack and num > stack[-1][1]:
                    return True 

            if num > mini:
                stack.append((num, mini))


            mini = min(mini, num)

        return False
