# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        def helper(node, target, isFirstTarget=True):
            if not node:
                return
            if isFirstTarget:
                if node.val == target:
                    if node.right:
                        return helper(node.right, node.left, False)
                    else:
                        return node.left
                elif node.val < target:
                    node.right = helper(node.right, target)
                else:
                    node.left = helper(node.left, target)
                return node
            else:
                if node.left:
                    node.left = helper(node.left, target, False)
                    return node
                else:
                    node.left = target
                    return node

        return helper(root, key)


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def successor(node):
            node = node.right
            while node.left:
                node = node.left
            return node.val

        def predecessor(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val

        def delete(node, val):
            if not node:
                return None
            if node.val > val:
                node.left = delete(node.left, val)
            elif node.val < val:
                node.right = delete(node.right, val)
            else:
                if not node.left and not node.right:
                    node = None
                elif node.right:
                    node.val = successor(node)
                    node.right = delete(node.right, node.val)
                elif node.left:
                    node.val = predecessor(node)
                    node.left = delete(node.left, node.val)
            return node

        return delete(root, key)

