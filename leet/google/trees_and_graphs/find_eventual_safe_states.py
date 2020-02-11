# both solution are the same
# The idea is to understand if there is a cycle
# in this algorithm once the node in res, this means it has safe path
# if the node not in res but in visited the node does not have safe path
# if node not in res and not in visited the node is not explored yet

class Solution:
    def eventualSafeNodes(self, graph: list) -> list:
        if not graph:
            return graph

        visited = set()
        res = set()

        def find(i):
            if i in res:
                return True
            if i in visited:
                return False
            visited.add(i)
            for child in graph[i]:
                # NOTE: if child does not contain safe node
                # so the parent and we return False
                if not find(child):
                    return False
            res.add(i)
            return True

        # we need this loop here to cover standalone nodes
        for i in range(len(graph)):
            if i not in visited:
                find(i)
        return sorted(res)


import collections

# in the above code we maintain two sets res and visited
# instead of having two sets this code maintain dictionary
# and the value are WHITE, GRAY, BLACK
# the rest of idea is the same
class Solution:
    def eventualSafeNodes(self, graph: list) -> list:
        if not graph:
            return graph
        WHITE, GRAY, BLACK = 0, 1, 2
        d = collections.defaultdict(int)

        def find(i):
            if d[i] != WHITE:
                return d[i] == BLACK

            d[i] = GRAY
            for child in graph[i]:
                if d[child] == BLACK:
                    continue
                if d[child] == GRAY or not find(child):
                    return False
            d[i] = BLACK
            return True

        for i in range(len(graph)):
            if i not in d:
                find(i)
        return sorted([k for k, v in d.items() if v == BLACK])


if __name__ == "__main__":
    s = Solution()
    s.eventualSafeNodes([[0], [2, 3, 4], [3, 4], [0, 4], []])
    # s.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])
    # s.eventualSafeNodes([[1,2,3,4],[1,2],[3,4],[0,4],[]])
    print('done')
