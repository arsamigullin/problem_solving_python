# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        root = TreeNode()
        stack = [root]

        i = 0
        while i < len(s):
            node = stack.pop()
            if s[i] == '-' or s[i].isdigit():
                node.val, i = self._getNumber(i, s)

                if i < len(s) and s[i] == '(':
                    stack.append(node)
                    node.left = TreeNode()
                    stack.append(node.left)

            elif node.left and s[i] == '(':
                stack.append(node)
                node.right = TreeNode()
                stack.append(node.right)

            i += 1
        return stack.pop() if stack else root

    def _getNumber(self, i, s):
        j = i
        while i < len(s) and (s[i] == '-' or s[i].isdigit()):
            i += 1

        return int(s[j:i]), i


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if not s:
            return None
        i = 0

        def helper():
            nonlocal i, s
            j = i
            while j < len(s) and (s[j] == '-' or s[j].isdigit()):
                j += 1
            val = int(s[i:j])
            node = TreeNode(val)
            i = j
            if i < len(s) and s[i] == '(':
                i += 1
                node.left = helper()
            if i < len(s) and s[i] == '(':
                i += 1
                node.right = helper()
            i += 1
            return node

        return helper()