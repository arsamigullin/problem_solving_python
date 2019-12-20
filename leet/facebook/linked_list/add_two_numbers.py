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

# when having such kind of task notice the condition
# "The digits are stored in reverse order and each of their nodes contain a single digit."
#  Having digits in reverse order is advantage, we do not need to reverse linked list
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
            # at this point carry is sum of values of l1 and l2
            # the calculation below needed to cover results that greater than 10
            # let say result is 16, then val for to store gonna be 16%10=6
            # and carry will  be 16//10 = 1
            # carry will be used in the next round
            l3.val = carry % 10
            carry = carry // 10

            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
        return head
if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    s.addTwoNumbers(l1, l2)