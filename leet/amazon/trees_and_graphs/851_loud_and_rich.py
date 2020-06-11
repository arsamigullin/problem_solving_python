import collections
from typing import List


# this is correct fast solution
class Solution:
    '''
    sometimes we have to compose the graph correctly
    richer contains edges where left vertex has more money than right one
    we can compose directed graph in two ways
    1. we can have left node to be the parent and right node to be tha child
    2. or we can do right node to be the parent and left node to be the child

    when doing the first way we will get a stuck (see the soluiton right below)

    having the right person to be parent gives us opportunity to find the quieter person without doubling our job
    each node needs to be visited only once and if it has been already visited just return the quiet person
    associated with it
    '''
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        ans = [N] * N
        graph = collections.defaultdict(list)
        for u, v in richer:
            graph[v].append(u)

        def dfs(node):
            if ans[node] == N:
                ans[node] = node
                for child in graph[node]:
                    cand = dfs(child)
                    if quiet[cand] < quiet[ans[node]]:
                        ans[node] = cand
            return ans[node]

        return list(map(dfs, range(N)))


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        N = len(quiet)
        ans = [i for i in range(N)]
        # 1. we can have left node to be the parent and right node to be tha child
        graph = collections.defaultdict(list)
        for u, v in richer:
            graph[u].append(v)
        # here we put the person who is quiet than its child
        def dfs(node, person):
            if quiet[person] < quiet[ans[node]]:
                ans[node] = person

            for child in graph[node]:
                dfs(child, person)
        # doint the richer person parent makes us constantly updating the children if we got more quiet parent
        for u, v in richer:
            if quiet[u] < quiet[v]:
                dfs(v, u)
            else:
                if ans[u] == N:
                    ans[u] = u
        return ans