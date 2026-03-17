class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}
        res= []

        for num in nums2:
            if not stack:
                stack.append(num)

            elif stack and num < stack[-1]:
                stack.append(num)

            while stack and num > stack[-1]:
                map[stack[-1]] = num
                stack.pop()
            stack.append(num)

        while stack:
            map[stack[-1]] = -1
            stack.pop()

        print(map)

        for n in nums1:
            res.append(map[n])


        return res

