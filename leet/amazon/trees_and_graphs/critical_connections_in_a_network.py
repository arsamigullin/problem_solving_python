import typing
import collections
List = typing.List
class SolutionGreek:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        visited = collections.defaultdict(bool)
        parents = collections.defaultdict(int)
        discovered = collections.defaultdict(int)
        low = collections.defaultdict(int)
        time = 0
        res = []

        def find_critical_path(u):
            visited[u] = True
            discovered[u] = time
            low[u] = time
            time += 1

            for v in graph[u]:
                if visited[v] == False:
                    parents[v] = u 
                    find_critical_path(v)
                    low[u] = min(low[u], low[v])
                    if low[v]>discovered[u]:
                        res.append([v,u])

                elif v!= parents[u]:
                    low[u] = min(low[u], low[v])
        
        for v in graph:
            if visited[v]==False:
                find_critical_path(v)
        
        return res


class SolutionFast:
    '''
    Algo
    1. Build graph
    2. Initialize level collection with n (n means the node has not been descovered yet)
    3. Start with whatever node and do DFS
    4. Each recursive function call contains the parent(to avoid call parent), the level to assign to the current node,
        and current node
    5. When traversing the children of node we update the level of the current node with  min(current_node_level, actual_child_level)
        if the path is critical actual_child_node will be equal to expected_child_node. This means none of the nodes of subtree
        has back edge to the parent node
    '''
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        
        #Building our graph
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)
        
        levels = [n] * n
        critical = []
        
        def dfs(node, level, parent):
            if levels[node] == n:
                #This indicates an undiscovered node.  The default discovery time is the one assigned by the parent
                levels[node] = level #Tentatively mark ourselves with the group level assigned to us by our parent.
                expected_child_level = level + 1 #We tentatively expect our children to belong to a group one level above our group
                
                #Looping through children
                for neighbor in graph[node]:
                    #Skip the parent
                    if neighbor != parent:
                        actual_child_level = dfs(neighbor, expected_child_level, node)
                        if actual_child_level == expected_child_level:
                            critical.append((node, neighbor))
                        levels[node] = min(levels[node], actual_child_level)    #This is the key point:
                        #If any of our children were found to be part of a lower-level group, then we are part of that group as well!
            return levels[node]    #At this point, groupLevels[node] represents the lowest level group that this node was found to be connected to
        
        dfs(3, 0, -1)
        return critical

if __name__ == "__main__":
    s = SolutionFast()
    s.criticalConnections(4,[[0,1],[1,2],[2,0],[1,3]])