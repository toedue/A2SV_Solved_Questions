class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        first_sum = sum(n for n in nums if n % 2 == 0)

        for i in range(len(queries)):
            index = queries[i][1]
            val = queries[i][0]

            # remove old value if it was even
            if nums[index] % 2 == 0:
                first_sum -= nums[index]

            current_sum = nums[index] + val
            nums[index] = current_sum

            # add new value if it is even
            if current_sum % 2 == 0:
                first_sum += current_sum
            
            result.append(first_sum)

        return result
