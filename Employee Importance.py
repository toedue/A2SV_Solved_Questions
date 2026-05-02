"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        emp_map = {}
        for emp in employees:
            emp_map[emp.id] = emp

        print(emp_map)

        total = 0
        queue = deque()
        queue.append(id)

        while queue:
            curr_id = queue.popleft()
            curr_emp = emp_map[curr_id]

            total += curr_emp.importance

            for sub_id in curr_emp.subordinates:
                queue.append(sub_id)

        return total

        return 0
        
