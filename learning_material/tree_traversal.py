# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def compose_tree(l, i):
    if i >= len(l) or l[i] is None:
        return None
    root = TreeNode(l[i])
    root.left = compose_tree(l, 2 * i + 1,)
    root.right = compose_tree(l, 2 * i + 2)
    return root
inbucket = []
def inorder(root):
    if root:
        inorder(root.left)
        inbucket.append(root.val)
        inorder(root.right)
postbucket = []
def postorder(root):
    if root:

        postorder(root.left)
        postorder(root.right)
        postbucket.append(root.val)
if __name__ == "__main__":
    node = compose_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 0)
    inorder(node)
    print(f"inorder {inbucket}")
    postorder(node)
    print(f"postorder {postbucket}")

