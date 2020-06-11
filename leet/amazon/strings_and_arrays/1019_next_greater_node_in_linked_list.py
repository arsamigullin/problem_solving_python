# Definition for singly-linked list.
from typing import List

# monotonous stack

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:

        stack = []
        size = 0
        node = head
        while node:
            node = node.next
            size += 1

        answer = [0] * size
        node = head

        i = 0
        while node:
            while stack and stack[-1][1] < node.val:
                index, val = stack.pop()
                answer[index] = node.val
            stack.append((i, node.val))
            node = node.next
            i += 1

        while stack:
            index, val = stack.pop()
            answer[index] = 0

        return answer