class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        max_radius = 0
        houses.sort()
        heaters.sort()

        def binary_search(num, heaters):
            position = len(heaters)
            left = 0
            right = len(heaters) - 1
            while(left <= right):
                mid = (left + right)//2

                if heaters[mid] >= num:
                    position = mid
                    right = mid - 1
                else: # heaters[mid]< num:
                    left = mid + 1

            return position


        for house in houses:
            right_index = binary_search(house, heaters)

            right_distance = float("inf")
            left_distance = float("inf")

            if right_index < len(heaters):
                right_distance = abs(house-heaters[right_index])

            if right_index > 0:
                left_distance = abs(house - heaters[right_index - 1])

            closest = min(right_distance, left_distance)
            max_radius = max(max_radius, closest)

        return max_radius

