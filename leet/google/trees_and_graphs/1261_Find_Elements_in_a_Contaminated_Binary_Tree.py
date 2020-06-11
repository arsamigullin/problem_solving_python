# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class FindElementsMy:

    def __init__(self, root: TreeNode):

        self.arr = []

        def dfs(node, val):
            if not node:
                return
            node.val = val
            self.arr.append(val)
            dfs(node.left, 2 * node.val + 1)
            dfs(node.right, 2 * node.val + 2)

        dfs(root, 0)
        self.arr.sort()
        # print(self.arr)

    def find(self, target: int) -> bool:
        lo = 0
        hi = len(self.arr) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if self.arr[mid] == target:
                return True
            elif self.arr[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return False

# O(1) using set
class FindElements:

    def __init__(self, root: TreeNode):
        self.ls = set()
        self.helper(root, 0)

    def helper(self, root, val):
        if not root:
            return
        root.val = val
        self.ls.add(val)
        self.helper(root.left, 2 * val + 1)
        self.helper(root.right, 2 * val + 2)

        # return root

    def find(self, target: int) -> bool:
        return target in self.ls

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)