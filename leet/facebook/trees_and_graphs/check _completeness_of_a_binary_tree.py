
# the best way to understand the this solution is to use some examples
# Before, let's mention that we have marker v. It will assign unique number to each of the node and regardless completeness
# it will always have the same values regardless of tree completness, for example
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
# if we have a perfect tree OR if all the leaves are as left as possible the len of stack will equal v from the latest node pasted to the stack
# But if we have gaps in the lowest level meaning the leaves are not as left as possible the length of stack will be less that v from lates node
class Solution(object):
    def isCompleteTree(self, root):
        nodes = [(root, 1)] #stack
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2 * v))
                nodes.append((node.right, 2 * v + 1))

        return nodes[-1][1] == len(nodes)


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
