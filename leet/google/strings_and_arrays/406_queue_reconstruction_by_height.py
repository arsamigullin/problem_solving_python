import heapq
from typing import List

class Solution1:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # here we sort people by height (tallest persons will be first) and then by count
        # count is basically the position at which the current person will be inserted
        # Let's now consider a queue with people of two different heights: 7 and 6. For simplicity, let's have just one 6-height guy.
        # First follow the strategy above and arrange guys of height 7. Now it's time to find a place for the guy of height 6.
        # Since he is "invisible" for the 7-height guys, he could take whatever place without disturbing 7-height guys order.
        # However, for him the others are visible, and hence he should take the position equal to his k-value, in order to have his proper place.
        people.sort(key = lambda x: (-x[0], x[1]))
        output = []
        for p in people:
            output.insert(p[1], p)
        return output


# this is still bad solution
class Solution2:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sorted_by_height = sorted(people, key=lambda x: x[0])
        print(sorted_by_height)
        sorted_by_count = sorted(people, key = lambda x: (-x[0], x[1]))
        print(sorted_by_count)
        res = [None] * len(people)

        for h, k in sorted_by_height:
            i = 0
            cur_max = 0
            while i < len(res):
                # if current cell is already busy
                #
                if res[i]:
                    cur_max += 1 if res[i][0] >= h else 0
                # by this we make sure that there are at least k persons that tallest than current h
                # recall that k points to the count of people that tallest of the current person
                elif i - k >= 0 and cur_max >= k:
                    res[i] = (h, k)
                    break
                else:
                    cur_max +=1

                i += 1
        return res




if __name__ == '__main__':
    s = Solution1()
    s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
    s.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]])
