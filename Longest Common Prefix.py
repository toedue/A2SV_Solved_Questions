class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # lexicographical sort
        strs.sort()

        first = strs[0]
        last = strs[-1]
        arr =[]

        if not strs:
            return ""

        if "" in strs:
            return ""

        for i , j in zip(first, last):
            if i == j:
                arr.append(i)
            else:
                break

        return "".join(arr)

        
