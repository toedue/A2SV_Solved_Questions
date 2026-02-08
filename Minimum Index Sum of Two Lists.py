class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}
        m = len(list1)
        n = len(list2)
        current = 0
        minimum = sys.maxsize
        arr = []
        for i in range(m):
            d[list1[i]] = i
        for j in range(n):
            if list2[j] in d:
                current = j + d[list2[j]]
                if current < minimum:
                    minimum = current
                    arr.clear()
                    arr.append(list2[j])
                elif current == minimum:
                    arr.append(list2[j])
        return arr
        

        
