# Definition for a binary tree node.
import re


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionMy:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        def dfs(expected_lvl):
            nonlocal i
            if i>=len(S):
                return None, False
            cur_lvl = 0
            while S[i] == '-':
                i+=1
                cur_lvl+=1
            if cur_lvl!= expected_lvl:
                i-=cur_lvl
                return None, False
            num = ''
            while i<len(S) and S[i] != '-':
                num+=S[i]
                i+=1
            node = TreeNode(int(num))
            l, found = dfs(cur_lvl+1)
            node.left = l
            if not found:
                return node, True
            r, found = dfs(cur_lvl+1)
            node.right = r
            return node, True
        return dfs(0)[0]


class Solution1:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        for i in range(30, -1, -1):
            if S.find('-' * i) != 0:
                S = S.replace('-' * i, chr(i + 65))

        def helper(s, depth):
            tmp = s.split(chr(depth + 65))
            root = TreeNode(tmp[0])
            root.left = helper(tmp[1], depth + 1) if len(tmp) > 1 else None
            root.right = helper(tmp[2], depth + 1) if len(tmp) > 2 else None
            return root

        return helper(S, 1)


class Solution2:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        vals = [(len(s[1]), int(s[2])) for s in re.findall("((-*)(\d+))", S)]

        def fn(level):
            if not vals or level != vals[0][0]:
                return None
            node = TreeNode(vals.pop(0)[1])
            node.left = fn(level + 1)
            node.right = fn(level + 1)
            return node

        return fn(0)

if __name__ == '__main__':
    s = Solution2()
    s.recoverFromPreorder("1-401--349---90--88")
