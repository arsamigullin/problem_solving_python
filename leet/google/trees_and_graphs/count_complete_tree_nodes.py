# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class SolutionFast:
    def countNodes(self, root: TreeNode) -> int:
        # optimized log n * log n
        # think about complete binary tree
        # - how to reduce searching, without visiting them all
        # - height is necessary,
        # - but leaf can be padded to the left
        #
        hasht = {}

        def get_height(node):
            if node is None:
                return 0
            if node in hasht:
                return hasht[node]
            else:
                tmp = 1 + get_height(node.left)
                hasht[node] = tmp
                return tmp

        def helper(node):
            if node is None:
                return 0
            lh = get_height(node.left)
            rh = get_height(node.right)
            if lh == rh:
                return 2**lh + helper(node.right)
            else:
                return 2**rh + helper(node.left)

        return helper(root)


def compose_tree(l, i):
    if i>=len(l) or l[i] is None:
        return None
    t = TreeNode(l[i])
    t.left = compose_tree(l, 2*i+1)
    t.right = compose_tree(l, 2 * i + 2)
    return t


root = compose_tree([1,2,3,4,5,6], 0)

# this is Brute force approach
# and this is not what you are expected to answer
class SolutionBrute:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1


class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        """
        Return tree depth in O(d) time.
        """
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists.
        Binary search with O(d) complexity.
        """
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: TreeNode) -> int:
        # if the tree is empty
        if not root:
            return 0

        d = self.compute_depth(root)
        # if the tree contains 1 node
        if d == 0:
            return 1

        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2 ** d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1

        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and left nodes on the last level.
        return (2 ** d - 1) + left

if __name__ == "__main__":
    s = Solution()
    s.countNodes(root)