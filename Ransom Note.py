class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1 = {}
        dict2 = {}
        for char in ransomNote:
            dict1[char] = dict1.get(char,0) + 1
        for char in magazine:
            dict2[char] = dict2.get(char,0) + 1

        can_construct = True
        for i in dict1:
            if dict1[i] > dict2.get(i,0):
                can_construct = False
                break
        return can_construct
            
