#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class SolutionMy:
    '''
    the approach here is
    reverse
    '''
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # rotate the whole list
        n = 0
        node = head
        while node:
            n += 1
            node = node.next
        if n == 0:
            return head
        k = k % n
        if k == 0:
            return head
        prev = None
        node = head
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
            n += 1

        def reverse(node, ends, i):
            if i >= len(ends):
                return node
            e = ends[i]
            cur = first = node
            prev = None
            s = 0
            while cur and s != e:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
                s += 1

            first.next = reverse(cur, ends, i + 1)
            return prev

        return reverse(prev, [k, None], 0)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # rotate the whole list
        if not head:
            return None
        if not head.next:
            return head

        old_tail = head
        n = 1
        # if we will find the old tail this way the node variable will be None
        # so we lost the reference to the old tail
        # node = head
        # n1 = 1
        # while node:
        #     node = node.next
        #     n1+=1
        # print(node)
        while old_tail.next:
            old_tail = old_tail.next
            n += 1

        # old_tail is ListNode(5)
        # and its next pointer will point to ListNode(1)
        # so we closed linked list
        # head is ListNode(1)
        old_tail.next = head

        # now we want to find new_tail
        # our list is 1,2,3,4,5 and k=2. We need to get 4,5,1,2,3
        # so new_tail must be 3 and it is located at n-k-1 position
        # because the elements n-k elements (i.e. 4,5 will be moved to the beginning of the list and 4 becomes a
        # new head)
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        # new_tail is 3
        # new_head is 4
        new_head = new_tail.next

        # we break loop here
        # new_tail is 3, and it is now pointing to None
        new_tail.next = None

        return new_head
if __name__ == "__main__":
    l = ListNode(1)
    l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = ListNode(4)
    l.next.next.next.next = ListNode(5)
    s = Solution()
    s.rotateRight(l,2)