from typing import List
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates




class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        empdict = {}
        for emp in employees:
            empdict[emp.id] = emp

        def helper(emp):
            if not emp:
                return 0
            tot = emp.importance
            for ch in emp.subordinates:
                tot += helper(empdict[ch])
            return tot

        return helper(empdict[id])

