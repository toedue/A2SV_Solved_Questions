class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        n = len(costs)
        res = 0
        costs.sort(key=lambda x:x[1]-x[0], reverse=True)

        print(costs)

        for i in range(n//2):
            res += costs[i][0]

        for i in range(n//2, n):
            res += costs[i][1]

        return res
    
