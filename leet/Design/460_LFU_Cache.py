from collections import defaultdict
from collections import OrderedDict


class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        del self.count2node[node.count][key]

        # clean memory
        if not self.count2node[node.count]:
            del self.count2node[node.count]

        node.count += 1
        self.count2node[node.count][key] = node

        # NOTICE check minCount!!!
        if not self.count2node[self.minCount]:
            self.minCount += 1

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.cap:
            return

        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key)  # NOTICE, put makes count+1 too
            return

        if len(self.key2node) == self.cap:
            # popitem(last=False) is FIFO, like queue
            # it return key and value!!!
            k, n = self.count2node[self.minCount].popitem(last=False)
            del self.key2node[k]

        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return


from collections import defaultdict, OrderedDict


class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count


class LFUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.key2node = {}
        self.key2count = defaultdict(OrderedDict)
        self.min_count = 0

    def get(self, key: int) -> int:

        if key in self.key2node:
            node = self.key2node[key]

            self.key2count[node.count].pop(key)
            if not self.key2count[node.count]:
                self.key2count.pop(node.count)
            node.count += 1
            self.key2count[node.count][key] = node

            if not self.key2count[self.min_count]:
                self.min_count += 1
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.size == 0:
            return
        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self.get(key)
            return
        elif len(self.key2node) >= self.size:
            k, _ = self.key2count[self.min_count].popitem(last=False)
            self.key2node.pop(k)
        self.key2count[1][key] = self.key2node[key] = Node(key, value, 1)
        self.min_count = 1


if __name__ == '__main__':
    s = LFUCache1(2)
    oper = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    data = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    oper = ["LFUCache", "put", "put", "put", "put", "get"]
    data = [[2], [3, 1], [2, 1], [2, 2], [4, 4], [2]]
    for i, o in enumerate(oper):
        if i == 0:
            s = LFUCache1(data[i][0])
            continue
        if o == "put":
            s.put(data[i][0],data[i][1])
        elif o == "get":
            s.get(data[i][0])

