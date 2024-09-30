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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        cnt = 1
        max_cnt = 0
        prev = -10 ** 6

        def check(val):
            nonlocal cnt, max_cnt, prev, res
            if val == prev:
                cnt += 1
            else:
                cnt = 1
            if cnt > max_cnt:
                res = [val]
            elif cnt == max_cnt:
                res.append(val)
            prev = val
            max_cnt = max(cnt, max_cnt)

        stack = []
        node = root
        while stack or node is not None:

            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                check(node.val)
                node = node.right

        # def dfs(node):

        #     if not node:
        #         return
        #     dfs(node.left)
        #     check(node.val)
        #     dfs(node.right)

        # dfs(root)
        return res

if __name__ == "__main__":
    s = Solution()
    t = TreeNode(1)
    t.right = TreeNode(2)
    t.right.left = TreeNode(2)
    s.findMode(t)
