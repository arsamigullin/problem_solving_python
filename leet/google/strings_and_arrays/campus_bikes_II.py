import typing
List = typing.List

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        bind = tuple(i for i in range(len(bikes)))
        d = {}
        def find(wi, bikes_to_be_visited):
            if bikes_to_be_visited in d:
                return d[bikes_to_be_visited]
            if wi >= len(workers):
                return 0
            m = float('inf')
            wx, wy = workers[wi]
            for i in range(len(bikes_to_be_visited)):
                bx, by = bikes[bikes_to_be_visited[i]]
                distance = abs(wx-bx) + abs(wy-by)
                m = min(m, find(wi + 1,bikes_to_be_visited[:i]+bikes_to_be_visited[i+1:] )+distance)
            d[bikes_to_be_visited] = m
            #print(diff, m, wi)
            #print(wi, left)
            return m
        return find(0, bind)


from functools import lru_cache


class SolutionLRU:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        # precompute distances
        dists = [[] for _ in range(len(workers))]
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                dists[i].append(dist)

        @lru_cache(None)
        def rec(i, visited):
            if i == len(workers):
                return 0

            sum_ = float('inf')
            for bike in range(len(bikes)):
                if not (visited & (1 << bike)):
                    visited |= (1 << bike)
                    dist = dists[i][bike]
                    sum_ = min(sum_, dist + rec(i + 1, visited))
                    visited &= ~(1 << bike)
            return sum_

        visited = 0

        return rec(0, visited)


class SolutionMemo(object):
    def assignBikes(self, workers, bikes):
        bikes = tuple(tuple(bike) for bike in bikes)
        memo = {}

        def rec_assign(worker_index, bikes):
            if worker_index == len(workers): return 0
            if bikes in memo: return memo[bikes]
            min_distance = float('inf')
            for i, (bx, by) in enumerate(bikes):
                d = abs(bx - workers[worker_index][0]) + abs(by - workers[worker_index][1])
                if d < min_distance:
                    d += rec_assign(worker_index + 1, bikes[:i] + bikes[i + 1:])
                    if min_distance > d: min_distance = d
            memo[bikes] = min_distance
            return min_distance

        return rec_assign(0, bikes)

if __name__ == "__main__":
    s= Solution()
    print(s.assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))