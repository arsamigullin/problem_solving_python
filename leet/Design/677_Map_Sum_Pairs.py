
# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
import collections


class MapSum1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(int)
        self.words = collections.defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        # if the value of the key has changed, then all associated prefixes should also be adjusted
        to_sub = self.words[key]
        for i in range(1, len(key ) +1):
            self.d[key[:i]] +=val - to_sub
        self.words[key] = val



    def sum(self, prefix: str) -> int:
        return self.d[prefix]

class TrieNode(object):
    __slots__ = 'children', 'score'
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum(object):
    def __init__(self):
        self.map = {}
        self.root = TrieNode()

    def insert(self, key, val):
        # if the value of the key has changed, then all associated prefixes should also be adjusted
        delta = val - self.map.get(key, 0)
        self.map[key] = val
        cur = self.root
        cur.score += delta
        for char in key:
            cur = cur.children.setdefault(char, TrieNode())
            cur.score += delta

    def sum(self, prefix):
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return 0
            cur = cur.children[char]
        return cur.score

if __name__ == '__main__':
    s = MapSum()
    s.insert("apple", 3)
    s.sum("ap")
    s.insert("app", 2)
    s.sum("ap")
