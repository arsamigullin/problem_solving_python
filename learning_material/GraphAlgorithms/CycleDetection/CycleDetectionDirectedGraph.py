# According to Cormen, "a directed graph is acyclic if and only if a depth-ﬁrst search yields no “back” edges (Lemma 22.11)."
# To detect back edges Cormen introduces three colors WHITE, GRAY and BLACK
# WHITE color means the vertex has not been visited yet
# GRAY means we found back edge, so the graph has a cycle
# BLACK color means the vertex has been visited and beyond this vertex no cycles detected
import collections
from typing import List

# 1. Tree edges are edges in the depth-ﬁrst forest G  . Edge .u; / is a tree edge if 
# was ﬁrst discovered by exploring edge .u; /.
# 2. Back edges are those edges u,v connecting a vertex u to an ancestor v in a
# depth-ﬁrst tree. We consider self-loops, which may occur in directed graphs, to
# be back edges.
# 3. Forward edges are those nontree edges  u,v connecting a vertex u to a de-
# scendant v in a depth-ﬁrst tree.
# 4. Cross edges are all other edges. They can go between vertices in the same
# depth-ﬁrst tree, as long as one vertex is not an ancestor of the other, or they can
# go between vertices in different depth-ﬁrst trees.

class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        # compose the graph
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)

        # to store colors for each vertex
        colors = [0] * n

        def dfs(node):
            if colors[node] == WHITE:
                colors[node] = GRAY
                for child in graph[node]:
                    # cycle detected
                    if not dfs(child):
                        return False
                colors[node] = BLACK
                return True
            else:
                return colors[node] == BLACK

        for i in range(n):
            if colors[i] == WHITE:
                if not dfs(source):
                    return False