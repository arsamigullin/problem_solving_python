# Python program to do inorder traversal without recursion and
# without stack Morris inOrder Traversal
# https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/

# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Iterative function for inorder tree traversal
def MorrisTraversal(root):
    # Set current to root of binary tree
    current = root

    while current is not None:

        if current.left is None:
            current.data,
            current = current.right
        else:
            # Find the inorder predecessor of current
            pre = current.left
            while pre.right is not None and pre.right != current:
                pre = pre.right

                # Make current as right child of its inorder predecessor
            if (pre.right is None):
                pre.right = current
                current = current.left

                # Revert the changes made in if part to restore the
            # original tree i.e., fix the right child of predecessor
            else:
                pre.right = None
                current.data,
                current = current.right

            # Driver program to test the above function


"""  
Constructed binary tree is 
            1 
          /   \ 
        2      3 
      /  \ 
    4     5 
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

MorrisTraversal(root)

# This code is contributed by Naveen Aili