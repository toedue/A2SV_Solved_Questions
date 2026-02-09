class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = []
        for char , ind in zip(s, indices):
            result.append((char,ind))

        sort_s = sorted(result, key = lambda x: x[1])

        return "".join(x[0] for x in sort_s)
