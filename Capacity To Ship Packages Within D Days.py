class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def checkCapacity(capacity, weights):
            day = 1
            current_sum = 0

            for weight in weights:
                if weight + current_sum > capacity:
                    day += 1
                    current_sum = weight
                else:
                    current_sum += weight

            return day <= days

        ans = -1 
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            if checkCapacity(mid, weights):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
