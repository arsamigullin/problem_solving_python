class Solution:
    # graph: List[List[int]]
    #  a graph is bipartite if the vertices can be
    # divided into two sets, A and B , with no two vertices in A adjacent and no
    # two vertices in B adjacent.

    # Algo
    # Big picture: Every neighbor gets colored the opposite color from the current node. If we find a neighbor colored
    # the same color as the current node, then our coloring was impossible.

    # we maintain color dict to store visited nodes with a particular color
    # if the node not in the color dict using DFS we mark their children with opposite color
    # if node in color and if its color coincides with the color of one of its children
    # the graph is not bipartite

    def isBipartite(self, graph) -> bool:
        color = {}
        for node in range(len(graph)):
            if node not in color:
                color[node] = 0
                stack = [node]
                # it is important to maintain stack within the parent
                # if we had the stack out of loop we would end up with always True
                # whenever we've met None graph
                while stack:
                    n = stack.pop()
                    for child in graph[n]:
                        if child not in color:
                            stack.append(child)
                            color[child] = color[n] ^ 1
                        elif color[child] == color[n]:
                            return False
        return True

if __name__ == "__main__":
    s = Solution()
    s.isBipartite([[2,3,4],[2,3,4],[0,1],[0,1],[0,1]])
    #s.isBipartite([[1,3], [0,2], [1,3], [0,2]])