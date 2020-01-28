# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Add node to carry only if cnt is 0
# if cnt > 0 this means the latest carry has duplicates
# and we take prev (which does not have duplicates) and assign to its next (prev.next) current element

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        cnt = 0
        carry = root = ListNode(float('inf'))
        prev = None
        while node is not None:
            if carry.val == node.val:
                cnt += 1
            elif cnt == 0:
                prev = carry
                carry.next = node
                carry = carry.next
            else:
                prev.next = node
                cnt = 0
                carry = prev.next

            node = node.next

        if cnt > 0:
            prev.next = node
            carry = prev.next

        return root.next