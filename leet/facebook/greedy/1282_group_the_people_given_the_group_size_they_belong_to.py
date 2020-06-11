import collections
from typing import List

# fastest
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = collections.defaultdict(list)
        for i, v in enumerate(groupSizes):
            d[v].append(i)
        res = []
        for k in d:
            for i, v in enumerate(d[k]):
                if i % k == 0:
                    res.append([v])
                else:
                    res[-1].append(v)
        return res

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i, v in enumerate(groupSizes):
            d[v] = d.get(v, 0) + 1
        gs = sorted([(v, i) for i, v in enumerate(groupSizes)])
        res = []
        for g, i in gs:
            if d[g] != 0 and d[g]%g == 0:
                res.append([i])
            else:
                res[-1].append(i)
            d[g]-=1
        return res


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = collections.defaultdict(list)
        for i, v in enumerate(groupSizes):
            d[v].append(i)
        res = []
        for k in d:
            while d[k]:
                res.append(d[k][:k])
                d[k] = d[k][k:]
        return res


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = head
        even = prev0 = node
        odd = prev1 = node.next
        while prev1:
            if prev0 and prev0.next:
                prev0.next = prev0.next.next
                if prev0.next:
                    prev0 = prev0.next
            if prev1.next:
                prev1.next = prev1.next.next
            prev1 = prev1.next
        prev0.next = odd
        return even


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node = head
        even = prev0 = node
        odd = prev1 = node.next
        while prev1 and prev1.next:
            prev0.next = prev1.next
            prev0 = prev0.next
            prev1.next = prev0.next
            prev1 = prev1.next
        prev0.next = odd
        return even

