class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:

        ps = [0 for x in range (len(s) + 1)]

        for l, r, d in shifts:
            ps[r + 1] += 1 if d else -1 
            ps[l] += -1 if d else 1
        # print (ps)

        ancii = [ord(x) - ord('a') for x in s]

        # print(ancii)
        
        current = 0
        for i in reversed(range(len(ps))):
            current += ps[i]
            ancii[i-1] += current

        # print(ancii)

        for i in range(len(ancii)):
            ancii[i] = chr(ancii[i] % 26 + 97)

        # print(ancii)

        return "".join(ancii)

        
            

        # return 0
