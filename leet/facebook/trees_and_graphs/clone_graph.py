from collections import  deque

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
#
from collections import deque

# Algo
# Using DFS we popleft the node
# and we create a new node with the the same value and we put in onto dict with key = curr_node.val if it is not there
# we traverse over the neighbors of the current node and we create new instances of the neighbors and put them to the
# the dictionary if they are not in the dictionary
# IMPORTANT: we append queue with the only neighbors that are not in dictionary
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #print(node)
        d={}
        queue = deque([node])
        while len(queue) > 0:
            curr_node = queue.popleft()
            if curr_node:
                if curr_node.val not in d:
                    d[curr_node.val] = Node(curr_node.val, [])
                new_parent = d[curr_node.val]
                for nei in curr_node.neighbors:
                    if nei.val not in d:
                        d[nei.val] = Node(nei.val, [])
                        queue.append(nei)
                    new_parent.neighbors.append(d[nei.val])
        return d[node.val]


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        visited = {}
        def dfs(node):
            copyNode = Node(node.val)
            visited[node] = copyNode
            for child in node.neighbors:
                if child in visited:
                    copyNode.neighbors.append(visited[child])
                else:
                    copyNode.neighbors.append(dfs(child))
            return copyNode
        return dfs(node)


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        d = {}

        def helper(node):
            if node.val in d:
                return d[node.val]
            nodeCopy = Node(node.val)
            d[node.val] = nodeCopy
            for nei in node.neighbors:
                nodeCopy.neighbors.append(helper(nei))
            return nodeCopy

        return helper(node)


n1 = Node(1, [])
n2 = Node(2, [])
n3 = Node(3, [])
n4 = Node(4, [])

n1.neighbors.append(n2)
n1.neighbors.append(n3)
n1.neighbors.append(n4)

n2.neighbors.append(n1)
n2.neighbors.append(n3)
n2.neighbors.append(n4)

n3.neighbors.append(n1)
n3.neighbors.append(n2)
n3.neighbors.append(n4)

n4.neighbors.append(n1)
n4.neighbors.append(n3)
n4.neighbors.append(n2)

if __name__ == "__main__":
    s = Solution()
    s.cloneGraph(n1)