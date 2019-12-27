from collections import  deque

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
#
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #print(node)
        d={}
        queue = deque([node])
        while len(queue) > 0:
            nd = queue.popleft()
            if nd:
                if nd.val not in d:
                    d[nd.val] = Node(nd.val, [])
                tmp = d[nd.val]
                for nb in nd.neighbors:
                    if nb.val not in d:
                        d[nb.val] = Node(nb.val, [])
                        queue.append(nb)
                    tmp.neighbors.append(d[nb.val])
        return d[node.val]

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