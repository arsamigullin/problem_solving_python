# Definition for a binary tree node.
import collections
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O (N^2)
class Solution:
    '''
    4##
    24###
    4##
    24###
    4##
    324###4##
    124###324###4##
    '''
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        d = collections.defaultdict(int)
        ans = []

        def helper(node):
            if not node:
                return '#'
            serial = f"{node.val}{helper(node.left)}{helper(node.right)}"
            print(serial)
            d[serial] += 1
            # since we need to find duplicates only
            if d[serial] == 2:
                ans.append(node)
            return serial

        helper(root)
        return ans

# O(n)
class Solution2:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        d = collections.defaultdict()
        d.default_factory = d.__len__
        count = collections.Counter()
        ans = []

        def helper(node):
            if node:
                # here key is node.val, helper(node.left), helper(node.right)
                #
                uid = d[node.val, helper(node.left), helper(node.right)]
                print(uid)
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        helper(root)
        print(d)
        return ans


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(4)
    s = Solution2()
    s.findDuplicateSubtrees(root)