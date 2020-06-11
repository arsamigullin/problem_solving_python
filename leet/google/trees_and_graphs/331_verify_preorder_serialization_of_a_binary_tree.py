class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1
        for node in preorder.split(','):
            slot -= 1
            if slot < 0:
                return False
            if node != '#':
                slot += 2
        return slot == 0


class Solution1:
    def isValidSerialization(self, preorder: str) -> bool:
        i = 0
        preorder = preorder.split(',')

        def helper():
            nonlocal i
            if i >= len(preorder):
                return
            if preorder[i] == '#':
                return
            i += 1
            helper()
            i += 1
            helper()

        helper()
        return i == len(preorder) - 1