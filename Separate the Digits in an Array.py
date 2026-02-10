class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        string = "".join(map(str,nums))
        return [int(x) for x in string]
