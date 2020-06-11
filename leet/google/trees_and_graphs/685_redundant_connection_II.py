import collections
from typing import List


class Solution1(object):
    '''
    Starting from a rooted tree with N-1 edges and N vertices, let's enumerate the possibilities for the added "redundant" edge.
    If there is no loop, then either one vertex must have two parents (or no edge is redundant.)
    If there is a loop, then either one vertex has two parents, or every vertex has one parent.
    '''
    def findRedundantDirectedConnection(self, edges):
        N = len(edges)
        parent = {}
        candidates = []
        # first we have to find candidates
        for u, v in edges:
            # if v is already has a parent
            if v in parent:
                # add v and its parent
                candidates.append((parent[v], v))
                # add v and current parent
                candidates.append((u, v))
            else:
                parent[v] = u
        # here we find the parent
        # the node which has no incoming edges
        # we also keep track of seen nodes
        def orbit(node):
            seen = set()
            while node in parent and node not in seen:
                seen.add(node)
                node = parent[node]
            return node, seen

        root = orbit(1)[0]

        # if no candidates found
        # go over cycle composed by the nodes
        # started from root
        if not candidates:
            cycle = orbit(root)[1]
            for u, v in edges:
                if u in cycle and v in cycle:
                    # return latest edge
                    ans = u, v
            return ans

        children = collections.defaultdict(list)
        for v in parent:
            children[parent[v]].append(v)

        # nodes numeration starts from 1, that is why first is True
        seen = [True] + [False] * N
        stack = [root]
        # if all the nodes have been visited
        # this means we can remove the latest element
        # [[2,1],[3,1],[4,2],[1,4]]
        while stack:
            node = stack.pop()
            if not seen[node]:
                seen[node] = True
                stack.extend(children[node])
        # since True is 1 and False is 0
        return candidates[all(seen)]

if __name__ == '__main__':
    s = Solution1()
    s.findRedundantDirectedConnection([[3,1],[2,1],[4,2],[1,4]])
    s.findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]])
    s.findRedundantDirectedConnection([[5,2],[5,1],[3,1],[3,4],[3,5]])

class Solution2:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def find(u):  # union find
            if p[u] != u:
                p[u] = find(p[u])
            return p[u]

        def detect_cycle(edge):  # check whether you can go from u to v (forms a cycle) along the parents
            u, v = edge
            while u != v and u in parents:
                u = parents[u]
            return u == v

        candidates = []  # stores the two edges from the vertex where it has two parents
        parents = {}
        for u, v in edges:
            if v not in parents:
                parents[v] = u
            else:
                candidates.append((parents[v], v))
                candidates.append((u, v))

        if candidates:  # case 2 & case 3 where one vertex has two parents
            return candidates[0] if detect_cycle(candidates[0]) else candidates[1]
        else:  # case 1, we just perform a standard union find, same as redundant-connection
            p = list(range(len(edges)))
            for edge in edges:
                u, v = map(find, edge)
                if u == v:
                    return edge
                p[u] = p[v]


# need to result in one root
# solution for directed graph to rooted tree
class Solution3:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [0] * (n + 1)  # direct parent
        roots = list(range(n + 1))  # root
        ranks = [0] * (n + 1)  # rank

        def find(x):
            while roots[x] != x:
                x = roots[x]
            return x

        # process the edges, can get either 0 or 2 candidates
        # 0 no node has 2 parents, but a loop
        # 2 when a node has 2 parents
        ans1 = None
        ans2 = None
        for edge in edges:
            u, v = edge
            if parents[v] == 0:
                parents[v] = u
            else:
                ans1 = (parents[v], v)  # prev one
                ans2 = (u, v)  # later one
                edge[0] = edge[1] = -1

        for edge in edges:
            u, v = edge
            if u < 0 or v < 0:
                continue

            u = find(u)
            v = find(v)
            if u == v:
                return edge if not ans1 else ans1
            if ranks[v] > ranks[u]:
                roots[u] = v
            elif ranks[v] == ranks[u]:
                ranks[u] += 1
                roots[v] = u
            else:
                roots[v] = u

        return ans2