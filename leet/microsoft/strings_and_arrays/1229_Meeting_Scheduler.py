from typing import List


class Solution:
    # O((m+n)log(m+n))
    # this solution work because of this statement in the problem
    # "It is guaranteed that no two availability slots of the same person intersect with each other"
    # Example [[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8
    # after joining and sorting we get [[0,15],[10,50],[60,70],[60,120],[140,210]]
    # According to that algo we start from the end and compare
    # slot[i + 1][0] + duration <= slot[i][1]
    # When condition is TRUE it is impossible to have slot[i+1] and slot[i] belongs to the same person
    # because of above's statement

    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slot = sorted(list(filter(lambda x: x[0] + duration <= x[1], slots1 + slots2)))

        for i in range(len(slot) - 1):
            if slot[i + 1][0] + duration <= slot[i][1]:
                return [slot[i + 1][0], slot[i + 1][0] + duration]
        return []


class SolutionMy:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()

        i = 0
        j = 0

        while i < len(slots1) and j < len(slots2):
            s1, e1 = slots1[i]
            s2, e2 = slots2[j]

            if s1 > e2:
                j += 1
                continue
            if s2 > e1:
                i += 1
                continue

            suitable_end = max(s1, s2) + duration
            if suitable_end <= e1 and suitable_end <= e2:
                return max(s1, s2), suitable_end
            i += 1
            j += 1
            diff1 = e1 - s1
            diff2 = e2 - s2

            if diff1 == diff2:
                i += 1
                j += 1
            elif diff1 < diff2:
                i += 1
            else:
                j += 1
        return []


class Solution2:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1 = [_ for _ in slots1 if _[1]-_[0]>=duration]
        slots2 = [_ for _ in slots2 if _[1]-_[0]>=duration]
        slots1.sort()
        slots2.sort()
        while slots1 and slots2:
            if slots1[0][0] > slots2[0][0] or (slots1[0][0] == slots2[0][0] and slots1[0][1] >= slots2[0][1]):
                first = slots2.pop(0)
                second = slots1[0]
            else:
                first = slots1.pop(0)
                second = slots2[0]
            if min(first[1], second[1]) - second[0] >= duration:
                return [second[0], second[0] + duration]
        return []

if __name__ == '__main__':
    s = Solution()
    s.minAvailableDuration([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8)
    s.minAvailableDuration([[10,50],[60,120],[140,210]], [[0,15],[60,70]], 8)