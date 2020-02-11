class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: TreeNode) -> list:
        res = []
        temp = [float('-inf'), float('-inf')]

        def find(node):
            nonlocal temp
            nonlocal res
            if node is None:
                return None
            find(node.left)
            if temp[1] == node.val:
                temp[0] += 1
            else:
                if res:
                    if res[-1][0] < temp[0]:
                        res = [temp[:]]
                    else:
                        res.append(temp[:])
                else:
                    res.append(temp[:])
                temp = [1, node.val]
            find(node.right)


        find(root)
        if res:
            if res[-1][0] < temp[0]:
                res = [temp[:]]
            else:
                res.append(temp[:])
        else:
            res.append(temp[:])
        return [res[1] for _ in res]

if __name__ == "__main__":
    s = Solution()
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(2)
    s.findMode(t)
