
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# This is my first solution. I use additional memory
# Algo
# 1. Using DFS (inorder traversal) collect all the nodes to the list
# All the nodes will be in the sorted order
# 2. Travers through the list and assign left(predecessor) and right(successor)
class SolutionMy:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        l = list()

        def get_nodes(node):
            if node is None:
                return
            get_nodes(node.left)
            l.append(node)
            get_nodes(node.right)

        get_nodes(root)
        if len(l) == 1:
            l[0].left = l[0]
            l[0].right = l[0]
            return l[0]
        head = l[0]
        for i in range(len(l)):
            if i == 0:
                l[i].right = l[i + 1]
                l[i].left = l[-1]
            elif i == len(l) - 1:
                l[i].right = l[0]
                l[i].left = l[i - 1]
            else:
                l[i].left = l[i - 1]
                l[i].right = l[i + 1]

        return l[0]

# Here we use InOrder traversal
#Algo
# 1. Traverse InOrder till the most left node of a tree
# if last is still None we haven't reached the most left node yet
# 2. Once left most node reached, we assign node to the first node
# the first will never overwritten anymore
# 3. Always assign cur node to the prev node
# 4. update prev.right = node and node.left = prev
# node.right will be updated at the right node
# 5. Do not forget to close DLL
# first.left = last
# last.right = first

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def convertToDll(node):
            nonlocal first, last
            if node:
                convertToDll(node.left)
                if last:
                    # Note here we assign only predecessor of current node
                    # successor of the current node will be assigned late
                    # when travelling to the right node
                    last.right = node
                    node.left = last
                else:
                    # this means we reached the most left node
                    first = node # this line will be assigned only once at the most left node of a tree
                last = node
                convertToDll(node.right)
        if root is None:
            return root
        first, last = None, None
        convertToDll(root)
        last.right = first
        first.left = last
        return first
l = [4,2,5,1,3]
def compose_tree(l, i):
    if i>=len(l) or l[i] is None:
        return None
    t = Node(l[i])
    t.left = compose_tree(l, 2*i+1)
    t.right = compose_tree(l, 2 * i + 2)
    return t
root = compose_tree(l,0)


class SolutionDFSStack:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                print(node.val)


class SolutionAttempt:
    def __init__(self):
        self.first = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        head = root

        def find(node):
            if node is None:
                return None
            l = find(node.left)

            if l is None:
                if self.first is None:
                    self.first = node
            else:
                print(f"l {l.val}")
                l.rigth = node
                node.left = l
            print(f"node {node.val}")
            r = find(node.right)
            if r is not None:
                print(f"r {r.val}")
                r.left = node
                node.right = r
            if r:
                return r
            else:
                return node

        last = find(head)
        print(f"last {last.val}")
        print(f"first {self.first.val}")
        self.first.left = last
        last.right = self.first
        return self.first

if __name__ == "__main__":
    s = SolutionAttempt()
    s.treeToDoublyList(root)
    s= SolutionDFSStack()
    s.treeToDoublyList(root)