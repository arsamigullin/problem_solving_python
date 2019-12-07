#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
class Solution:
    # my solution
    def removeNthFromEnd(head, n: int):
        node = head
        count = 0
        while node != None:
            node = node.next
            count += 1
        num_to_remove = count - n
        print(num_to_remove)
        node = head
        count = 1
        if num_to_remove == 0:
            return head.next
        while node != None:
            if count == num_to_remove:
                if node.next is None:
                    node.next = None
                else:
                    node.next = node.next.next
                break

            node = node.next
            count += 1
        return head

#their solution
