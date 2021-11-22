from heapq import *
import typing
List = typing.List
# Nice solution

# Algo
# We determine (min distance for nearest bike, bike) and collect them
# traversing over this collection we check if the bike has been already visited
# if it is not, we just assing this bike to the worker
# if it is (this means the same bike is going to be taken by other worker), we will search for another closest bike
# 390ms
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:

        def closest_bike(w_row, w_col):
            min_distance = 2001
            min_b_id = None

            for b_id, (b_row, b_col) in bikes.items():
                distance = abs(w_row - b_row) + abs(w_col - b_col)

                if distance < min_distance:
                    min_distance = distance
                    min_b_id = b_id

            return min_distance, min_b_id

        bikes = dict(enumerate(bikes))
        seen = set()
        assignment = [None] * len(workers)
        heap = []

        for w_id, (w_row, w_col) in enumerate(workers):
            distance, b_id = closest_bike(w_row, w_col)
            heappush(heap, (distance, w_id, b_id))

        while len(seen) < len(workers):
            _, w_id, b_id = heappop(heap)

            if b_id in seen:
                w_row, w_col = workers[w_id]
                distance, b_id = closest_bike(w_row, w_col)
                heappush(heap, (distance, w_id, b_id))

            else:
                assignment[w_id] = b_id
                seen.add(b_id)
                del bikes[b_id]

        return assignment

# 1800ms
class SolutionLong:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        bike_dict = [False] * len(bikes)
        worker_dict = [False] * len(workers)

        bw = []
        for i, w in enumerate(workers):
            for j, b in enumerate(bikes):
                bw.append([abs(w[0] - b[0]) + abs(w[1] - b[1]), i, j])
        bw.sort()
        # print(bw)
        res = [0] * len(workers)
        for d, i, j in bw:
            if not worker_dict[i] and not bike_dict[j]:
                res[i] = j
                worker_dict[i] = True
                bike_dict[j] = True
        return res


if __name__ == "__main__":
    s = Solution()
    s.assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]])
    #s.assignBikes([[0,0],[2,1]], [[1,2],[3,3]])