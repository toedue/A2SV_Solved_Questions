class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = sorted(strs, key = lambda x: len(x))

        first = x[0]
        last = x[-1]

        result = ""
        for i in range(len(first)):
            if first[i] != last[i]:
                break
            else:
                result += first[i]
        return result  




