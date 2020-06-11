import collections
from typing import List


class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        parent = {}
        size = {}
        for i, well in enumerate(wells):
            # the core idea is to add dummy edge
            # that will connect each house's well and its house
            # we probably could have as many fake node as house count
            # but instead it is better to have only one fake node(0)
            # from that 0 there will be edges representing the cost of installing well in that house
            # eventually we have a connected graph
            # we need to find minimum spanning tree of that graph
            pipes.append([0, i + 1, well])

        pipes.sort(key=lambda x: x[2])

        def find(p):
            parent.setdefault(p, p)
            size.setdefault(p, 1)
            root = p
            while root != parent[root]:
                root = parent[root]
            while root != p:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def union(p, q):
            nonlocal n
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]

        total_cost = 0
        for u, v, cost in pipes:
            if find(u) != find(v):
                union(u, v)
                total_cost += cost
        return total_cost


if __name__ == '__main__':
    s= Solution()
    s.minCostToSupplyWater(38,
[93151,20876,59743,57253,22852,68389,7424,54743,32955,39509,14896,54179,51356,78618,95595,69161,37790,67284,91644,91111,52096,61039,56597,70549,72491,90473,42299,76091,89905,31271,58546,48511,72171,78695,41038,81168,32922,49332],
[[2,1,21154],[3,2,81115],[4,3,94841],[5,2,96414],[6,3,72515],[7,5,52265],[8,1,60281],[9,5,47008],[10,6,83062],[11,1,83592],[12,11,29667],[13,5,43482],[14,8,68029],[15,6,29058],[16,14,14198],[17,8,61513],[18,10,96383],[19,3,12103],[21,11,51835],[22,8,14803],[23,22,30324],[24,23,63187],[25,21,62508],[26,13,86421],[27,22,59810],[28,6,80818],[29,25,350],[30,26,9676],[31,27,11396],[33,29,39112],[34,18,35099],[35,3,79588],[36,25,93238],[37,30,18366],[38,16,57918]])
    #s.minCostToSupplyWater(60,
#[93151,20876,59743,57253,22852,68389,7424,54743,32955,39509,14896,54179,51356,78618,95595,69161,37790,67284,91644,91111,52096,61039,56597,70549,72491,90473,42299,76091,89905,31271,58546,48511,72171,78695,41038,81168,32922,49332,637,7340,70333,20202,45698,64674,12549,46263,26798,1334,30355,83189,26439,51031,85145,56095,38430,79718,82385,25719,97525,82106],
#[[2,1,21154],[3,2,81115],[4,3,94841],[5,2,96414],[6,3,72515],[7,5,52265],[8,1,60281],[9,5,47008],[10,6,83062],[11,1,83592],[12,11,29667],[13,5,43482],[14,8,68029],[15,6,29058],[16,14,14198],[17,8,61513],[18,10,96383],[19,3,12103],[21,11,51835],[22,8,14803],[23,22,30324],[24,23,63187],[25,21,62508],[26,13,86421],[27,22,59810],[28,6,80818],[29,25,350],[30,26,9676],[31,27,11396],[33,29,39112],[34,18,35099],[35,3,79588],[36,25,93238],[37,30,18366],[38,16,57918],[39,36,14416],[40,25,27362],[41,5,12434],[42,9,5570],[43,42,72309],[44,8,81276],[45,44,2620],[46,44,57766],[47,11,71293],[48,40,14627],[49,48,33901],[52,49,70471],[53,38,6615],[55,19,77453],[56,9,63999],[57,34,10940],[58,29,43449],[59,43,22295],[60,5,84242]])
    #s.minCostToSupplyWater(6,[1,1,2,3,0,2],[[1,2,0],[2,3,2],[2,4,3],[2,5,2],[5,6,1]])