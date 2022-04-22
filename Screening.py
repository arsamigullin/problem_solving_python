'''
     5 (0)
  2 (1)     7 (2)
11 3   4  8
    17     9

5;2;7;11;3;4;8;17;9
#result [[5] [2 7] ..]
'''
# i*2 + 1
# i*2 + 2
# [1 2 3 4 5]

class TreeNode:
    def __init__(self, val, leftNode=None, rightNode=None):
        self.val = val
        self.left = leftNode
        self.rigth = rightNode

class Solution:
    def print_node_values(self, root, level):
        def print_dfs(node, cur_level):
            if not node:
                return False
            if cur_level == level:
                if node.val is not None:
                    print(node.val)
                    node.val = None
                    return True
                else:
                    return False
            elif cur_level < level:
                if not print_dfs(node.left, cur_level+1):
                    return print_dfs(node.right, cur_level+1)
                else:
                    return True
            return False

        print_dfs(root, level)

    def tree_hight(self,root):
        if not root:
            return 0
        return max(self.tree_hight(root.left),self.tree_hight(root.rigth)) + 1


if __name__ == '__main__':

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.rigth = TreeNode(5)
    root.left.left = TreeNode(7)
    root.left.rigth = TreeNode(9)
    root.rigth.rigth = TreeNode(10)

    s = Solution()
    prev = 0
    s.print_node_values(root, prev)
