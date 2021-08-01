import collections
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        prev_st = 0
        students = collections.deque(students)
        sandwiches = collections.deque(sandwiches)

        while len(students) != prev_st:
            prev_st = len(students)
            i = 0
            while students and i < len(students):
                if students[0] == sandwiches[0]:
                    students.popleft()
                    sandwiches.popleft()
                else:
                    students.append(students.popleft())
                i += 1
        return len(students)