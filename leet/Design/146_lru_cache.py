import bisect
import collections


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curcap = 0
        self.cache = {}
        self.latest = None
        self.first = None

    def move_to_end(self, key, val):
        if len(self.cache)<=1:
            return
        self.evict(key)
        self.curcap += 1
        if self.latest:
            self.cache[self.latest][1] = key
        if not self.first:
            self.first = key
        self.cache[key] = [self.latest, None, val]
        self.latest = key

    def get(self, key: int) -> int:
        value = self.cache.get(key, None)
        if value is None:
            return -1
        else:
            self.move_to_end(key, value[2])
            return value[2]

    def evict(self, key: int) -> int:
        value = self.cache.get(key, None)
        if value is None:
            return -1
        else:
            self.curcap -= 1
            prev, nxt, val = self.cache.pop(key)
            if nxt is not None:
                self.cache[nxt][0] = prev
            if prev is not None:
                self.cache[prev][1] = nxt
            if nxt is None:
                self.latest = prev
            if prev is None:
                self.first = nxt
            return val

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == 0:
            self.cache[key] = [None, None, value]
            self.latest = key
            self.first = key
            self.curcap += 1
        else:
            if key in self.cache:
                self.move_to_end(key, value)
                self.cache[key][2] = value
            else:
                if self.curcap == self.capacity:
                    self.evict(self.first)
                if self.latest and self.latest!=key:
                    self.cache[self.latest][1] = key
                if not self.first:
                    self.first = key
                self.cache[key] = [None if self.latest==key else self.latest, None, value]
                self.latest = key
                self.curcap += 1


from collections import OrderedDict


class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return - 1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class DoublyLinkedList:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.nxt = nxt
        self.prev = prev
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.dummy = DoublyLinkedList()
        self.last = self.dummy
        self.d = collections.defaultdict(DoublyLinkedList)

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            # we move to the end only if the key in self.d
            self._move_to_end(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self._move_to_end(node)
        else:
            node = DoublyLinkedList(key, value)
            self.d[key] = node
            self.last.nxt = node
            node.prev = self.last
            self.last = node
        # after the dummy, there will be at least 2 more nodes
        # because min capacity is 1
        if len(self.d) > self.size:
            node_to_del = self.d[self.dummy.nxt.key]
            self.dummy.nxt = node_to_del.nxt
            node_to_del.nxt.prev = self.dummy
            self.d.pop(node_to_del.key)

    def _move_to_end(self, node):
        # if the node is already last
        # do nothing
        if node == self.last:
            return
        # remove from the current position
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev
        # put to the end
        self.last.nxt = node
        node.prev = self.last
        self.last = node
        node.nxt = None


class ListNode:
    def __init__(self, val, key, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.head = ListNode(-1, -1)
        self.last = self.head
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self._update(key, self.d[key].val)
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # evict the LRU only if it is greater than capacity AND the key not in the d
        if len(self.d) >= self.size and key not in self.d:
            to_evict = self.head.nxt
            self.head.nxt = to_evict.nxt
            if to_evict.nxt:
                to_evict.nxt.prev = self.head
            self.d.pop(to_evict.key)
        self._update(key, value)

    def _update(self, key, value):

        if key in self.d:
            self.d[key].val = value
            # the current element is already the last one
            if not self.d[key].nxt:
                return
            cur = self.d.pop(key)
            prev_cur = cur.prev
            nxt_cur = cur.nxt
            prev_cur.nxt = nxt_cur
            nxt_cur.prev = prev_cur
        else:
            cur = ListNode(value, key)

        self.last.nxt = cur
        cur.prev = self.last
        cur.nxt = None
        self.last = cur
        self.d[key] = cur


if __name__ == '__main__':
    #["LRUCache", "put", "get", "put", "get", "get"]
    #[[1], [2, 1], [2], [3, 2], [2], [3]]

    #["LRUCache", "put", "put", "put", "put", "get", "get"]
    #[[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(1, 1)
    cache.put(2, 3)
    cache.put(4, 1)
    cache.get(1)
    cache.get(2)

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    cache.get(2)

    cache = LRUCache(1)
    cache.put(2, 1)
    cache.get(2)
    cache.put(3, 2)
    cache.get(2)
    cache.get(3)

    cache = LRUCache(1)
    cache.put(2,1)
    cache.get(2)

    cache = LRUCache(2)
    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);
    cache.put(3, 3);
    cache.get(2);
    cache.put(4, 4);
    cache.get(1);
    cache.get(3);
    cache.get(4);