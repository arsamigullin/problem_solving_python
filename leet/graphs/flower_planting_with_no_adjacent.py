#https://leetcode.com/problems/flower-planting-with-no-adjacent/
# Important conditions:
# paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.
# each flower connected no more that with 3 flowers
# we have only 4 types of flowers
# Algo:
# 1. convert the input in adjacency-list representation
# 2. for each flower in that list iterate over the neighbors and see if the neighbor is already set the type flower in
# flower_dist array
# 3. if it is set, remove this type of flower from flower_types
# 4. as each flower connected no more than with 3 flowers the flower_types will always have at least 1 element
# set any left type flower to the current flower

class Solution:
    def gardenNoAdj(self, N: int, paths: list) -> list:
        adj_list = [[] for _ in range(N + 1)]
        flower_dist = [0] * N
        for x, y in paths:
            adj_list[x].append(y)
            adj_list[y].append(x)

        for i in range(1, len(adj_list)):
            neighbors = adj_list[i]
            flower_types = [1, 2, 3, 4]
            for n in neighbors:
                if flower_dist[n - 1] != 0 and flower_dist[n - 1] in flower_types:
                    flower_types.remove(flower_dist[n - 1])

            flower_dist[i - 1] = flower_types[0]

        return flower_dist