class ListNode:
    def __init__(self, val, key, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.head = self.first = ListNode(-1, -1)
        self.last = self.head
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self._add(key, self.d[key].val)
            return self.d[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # evict the LRU
        if len(self.d) >= self.size:
            to_evict = self.head.nxt
            self.head.nxt = to_evict.nxt
            if to_evict.nxt:
                to_evict.nxt.prev = self.head
            else:
                self.last = self.head
            self.d.pop(to_evict.key)
        self._add(key, value)

    def _add(self, key, value):
        # print(key, value)
        cur = ListNode(value, key)
        if key in self.d:
            self.d[key].val = value
            if not self.d[key].nxt:
                return

            cur = self.d.pop(key)
            cur.val = value
            prev_cur = cur.prev
            nxt_cur = cur.nxt
            prev_cur.nxt = nxt_cur
            nxt_cur.prev = prev_cur
        self.last.nxt = cur
        cur.prev = self.last
        cur.nxt = None
        self.last = cur
        self.d[key] = cur


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    s = LRUCache(2)
    s.put(2,6)
    s.put(1,5)
    s.get(1)
    s.put(1,2)
    s.get(1)
    s.get(2)