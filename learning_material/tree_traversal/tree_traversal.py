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

##########recursive#############
inbucket = []
def inorder(root):
    if root:
        inorder(root.left)
        inbucket.append(root.val)
        inorder(root.right)

prebucket = []
def preorder(root):
    if root:
        prebucket.append(root.val)
        preorder(root.left)
        preorder(root.right)


postbucket = []
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        postbucket.append(root.val)

##########iterative###############

dfsIterativePreOrderBucket = []
def dfsIterativePreorder(root):
    stack = []
    node = root
    while stack or node is not None:
        if node is None:
            node = stack.pop()
            node = node.right
        else:
            dfsIterativePreOrderBucket.append(node.val)
            stack.append(node)
            node = node.left

def dfsIterativeAnotherOptionPreorder(root):
    node = root
    stack = [node]

    while stack:
        if node is None:
            node = stack.pop()
            node = node.right
        else:
            dfsIterativePreOrderBucket.append(node.val)
            stack.append(node)
            node = node.left

dfsIterativeInorderBucket = []
def dfsIterativeInorder(root):
        stack = []
        node = root
        while stack or node is not None:
            if node is None:
                node = stack.pop()
                dfsIterativeInorderBucket.append(node.val)
                node = node.right
            else:
                stack.append(node)
                node = node.left



dfsIterativePostOrderBucket = []
def dfsIterativePostorder(root):
    stack = [root]
    while stack:
        node = stack.pop()
        dfsIterativePostOrderBucket.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

# sometimes it is much better to use simple implementation
        while stack or node:
            node, curnum = stack.pop()
            if node is not None:
                if node.left is None and node.right is None:
                    curnum = curnum * 10+node.val
                    val += curnum
                else:
                    stack.append(node.left)
                    stack.append(node.right)
        return sum(nums)

if __name__ == "__main__":
    node = compose_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], 0)
    #node = compose_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ], 0)
    preorder(node)
    print(f"preorder {prebucket}")
    inorder(node)
    print(f"inorder {inbucket}")
    postorder(node)
    print(f"postord {postbucket}")
    dfsIterativeInorder(node)
    print(f"inoIter {dfsIterativeInorderBucket}")
    dfsIterativePreorder(node)
    print(f"preIter {dfsIterativePreOrderBucket}")
    dfsIterativePostorder(node)
    print(f"posIter {list(reversed(dfsIterativePostOrderBucket))}")

