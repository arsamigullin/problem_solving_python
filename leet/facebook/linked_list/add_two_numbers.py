# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def addTwoNumbers(self, l1, l2):

        def getNums(l):
            num = ""
            node = l
            while node is not None:
                num = str(node.val) + num
                node = node.next
            print(num)
            return int(num)

        num1 = getNums(l1)
        num2 = getNums(l2)

        total = str(num1 + num2)[::-1]
        root = ListNode(0)
        node = root
        for i in range(len(total)):

            node.val = total[i]
            if i != len(total) - 1:
                node.next = ListNode(0)
                node = node.next

        return root

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        carry = 0
        while (l1 or l2 or carry):
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            l3.val = carry % 10
            carry = carry // 10
            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
        return head