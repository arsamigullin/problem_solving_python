#https://leetcode.com/problems/delete-node-in-a-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.

        for example we have a list [4,5,1,9]
        the node is [5,1,9]
        We override node.val with the next val, i.e. we put 1 instead of 5
        node.next will be 9 (node.next.next)
        i.e. 1.next = 9
        overall
        1, 9
        """

        node.next, node.val = node.next.next, node.next.val
