
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


# let's call it as Brute force approach
class Solution1:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        root = node = Node(0, None, 0)
        carry = head
        while carry:
            node.next = Node(carry.val, None, carry.random)
            node = node.next
            carry = carry.next

        node1 = root.next
        carry = head
        while carry:
            tmp = None
            node2 = root.next
            if carry.random is not None:
                while node2:
                    if carry.random.val == node2.val:
                        tmp = node2
                        break
                    node2 = node2.next
            node1.random = tmp
            carry = carry.next
            node1 = node1.next

        return root.next

class Solution(object):
    """
    :type head: Node
    :rtype: Node
    """
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}
    # the important thing here is that initially we are storing in visitedHash all the next nodes by calling
    # self.copyRandomList(head.next), i.e. we have all the nodes in visitedHash now
    # note: key in visitedHash is node from original linked list
    # then we are processing random nodes and as all the nodes that have been visited are in visitedHash
    # copyRandomList will always return self.visitedHash[head] or None
    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

if __name__ == "__main__":
    n1 = Node(1, None, None)
    n1.next = n2 = Node(2, None, None)
    n2.next = n3 = Node(3, None, None)
    n3.next = n4 = Node(4, None, None)
    n1.random = n4
    n2.random = n1
    n3.random = n3
    n4 = n2
    my_solution = Solution1()
    ns1 = my_solution.copyRandomList(n1)
    my_equal = ns1 == ns1.next.random #true
    solution = Solution()
    ns2 = solution.copyRandomList(n1)
    equal = ns2 == ns2.next.random #true

