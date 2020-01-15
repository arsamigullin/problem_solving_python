
# the best way to understand this solution is to use some examples
# Before, let's mention that we have marker v. It will assign unique number
# to each of the node and regardless completeness
# it will always have the same values regardless of tree completeness, for example
# tree
#     1         1
#    / \       /
#   2   3     2
#  /           \
# 4             5

# for the first tree v for each node is
# 1-1, 2-2, 2-3, 4-4
#for the second tree v for each node is
# 1-1, 2-2, 5-5

# the only thing that will be changed when traversing the tree will be the stack length
# if we have a perfect tree OR if all the leaves are as left as possible the len
# of stack will equal v from the latest node pasted to the stack
# But if we have gaps in the lowest level meaning the leaves are not as left
# as possible the length of stack will be less that v from lates node
class Solution(object):
    def isCompleteTree(self, root):
        nodes = [(root, 1)] #stack
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                # Note how we assign order number
                # this is correct because it will cover LEFT and RIGHT nodes
                # Note we also adding None nodes here with an appropriate numbers
                nodes.append((node.left, 2 * v))
                nodes.append((node.right, 2 * v + 1))

        return nodes[-1][1] == len(nodes)
import collections
class Solution:
    def isCompleteTree(self, root) -> bool:
        q = collections.deque([(root, 0)])
        count = 0
        max_order = 0
        while q:
            node, order = q.popleft()
            max_order = max(max_order, order)
            if node:
                count+=1
                if node.left:
                    q.append((node.left, 2*order + 1))
                if node.right:
                    q.append((node.right, 2*order + 2))
        return max_order == count - 1

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compose_tree(l, i):
    if i >= len(l) or l[i] is None:
        return None
    return TreeNode(l[i], compose_tree(l, 2 * i + 1), compose_tree(l, 2 * i + 2))


#l = [1, 2, 3, None, None, 4, 5, None, None, None, None, 6, 7, 8, 9]
l = [1, 2, 3, 4, 5, 6]

tree = compose_tree(l,0)

if __name__ =="__main__":
    s = Solution()
    s.isCompleteTree(tree)
