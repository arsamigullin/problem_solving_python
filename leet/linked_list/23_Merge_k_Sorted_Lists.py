from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
            print(interval)
        return lists[0] if amount > 0 else None

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next


# Definition for singly-linked list.
from queue import PriorityQueue


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from queue import PriorityQueue


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        count = 0
        for l in lists:
            if l:
                q.put((l.val, count, l))
            count += 1
        while not q.empty():
            val, _, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, count, node))
            count += 1
        return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        prev = None
        for node in lists:
            head = loc_res = ListNode(-1)
            while node or prev:
                if prev and node:
                    if prev.val >= node.val:
                        loc_res.next = node
                        node = node.next
                    else:
                        loc_res.next = prev
                        prev = prev.next
                    loc_res = loc_res.next
                elif prev:
                    loc_res.next = prev
                    prev = prev.next
                    loc_res = loc_res.next
                elif node:
                    loc_res.next = node
                    node = node.next
                    loc_res = loc_res.next

            prev = head.next
        return prev

if __name__ == '__main__':
    s = Solution()

    import random
    totsize = 14
    lists = []
    for i in range(totsize):
        node = head = ListNode(-1)
        n = random.randint(0,18)
        vals = []
        for i in range(n):
            vals.append(random.randint(0,100))
        vals.sort()
        print(vals)
        for k in range(len(vals)):
            node.next = ListNode(vals[k])
            node = node.next
        lists.append(head.next)

    s.mergeKLists(lists)

