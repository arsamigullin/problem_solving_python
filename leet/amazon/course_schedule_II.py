import collections
import typing
List = typing.List
class Solution:

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        initCourses = [True] * numCourses
        if not any(initCourses):
            return []
        d = {}
        for s, f in prerequisites:
            initCourses[s] = False
            if s in d:
                d[s].append(f)
            else:
                d[s] = [f]
            if f not in d:
                d[f] = []
        visited = collections.defaultdict(int)
        courses = []
        WHITE, GRAY, BLACK = 0, 1, 2

        def find(id):
            if visited[id] != WHITE:
                return visited[id] == BLACK
            visited[id] = GRAY
            for child in d[id]:
                if not find(child):
                    return False
            visited[id] = BLACK
            courses.append(id)
            return True

        for i, v in enumerate(initCourses):
            if not v and not find(i):
                return []

        for i, v in enumerate(initCourses):
            if v and i not in visited:
                courses.append(i)

        return courses