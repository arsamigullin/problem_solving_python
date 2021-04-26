# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        first_part = self.find_first_part(head)
        second_part = self.reverse(first_part.next)

        f = head
        s = second_part
        while s and f:
            if s.val != f.val:
                return False
            s = s.next
            f = f.next
        return True

    def find_first_part(self, head):
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self, head):
        node = head
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp

        return prev


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr = head
        count = 0
        while curr != None:
            curr = curr.next
            count += 1
        is_odd = count % 2 == 1
        count = count // 2 + 1 if count % 2 == 1 else count / 2

        curr = head
        prev = None
        next_ = None
        while count != 0:
            next_ = curr.next
            if count != 1 or is_odd == False:
                curr.next = prev
                prev = curr
            curr = next_
            count -= 1

        while next_ != None:
            if next_.val != prev.val:
                return False

            next_ = next_.next
            prev = prev.next

        return True



