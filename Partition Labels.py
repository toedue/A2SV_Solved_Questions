class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        size = len(s)

        for indx, chr in enumerate(s):
            d[chr]  = indx
        res = []
        temp = 0
        start = 0

        for i in range(len(s)):
            temp = max(temp, d[s[i]])
            if i == temp:
                res.append(s[start:i+1])
                start = i + 1

        return [len(x) for x in res]
       
