class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # position = haystack.find(needle)
        # return position
        n = len(needle)

        for i in range(len(haystack) - n + 1):
            window = haystack[i:i+n]
            if window == needle:
                return i

        return -1

        







        
"""
.find() or .index()
Returns the position of the first match (or -1 if not found).
but  for .index() if the substring is not found, it raises an error instead of -1.
""" 
