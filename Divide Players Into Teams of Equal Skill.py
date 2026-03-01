class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        size = len(skill)

        if size == 1 or size % 2 == 1 or size ==0:
            return -1

        skill.sort()
        ptr1, ptr2 = 0, size -1
        team = skill[ptr2] + skill[ptr1]
        flag = True
        ans = 0

        while ptr1 < ptr2:
            if team != skill[ptr2] + skill[ptr1]:
                return -1
            else:
                ans += skill[ptr2] * skill[ptr1]
                ptr1 += 1
                ptr2 -= 1
        return ans
            


        
