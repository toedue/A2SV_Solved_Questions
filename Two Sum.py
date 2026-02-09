class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1

        d = [(v,k) for k,v in enumerate(nums)]
        # return d

        d.sort()

        while (l < r):
            if d[l][0] + d[r][0] > target:
                r -= 1
            elif d[l][0] + d[r][0] < target:
                l+= 1
            elif d[l][0] + d[r][0] == target:
                return [d[l][1] , d[r][1]]
 
