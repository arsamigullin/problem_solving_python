from typing import List


class StreamChecker1:

    def __init__(self, words: List[str]):
        self.pointers = []
        self.trie = {}
        for word in words:
            node = self.trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = '#'
        print(self.trie)

    def query(self, letter: str) -> bool:
        found = False
        for i in range(len(self.pointers)):
            if letter in self.pointers[i]:
                self.pointers[i] = self.pointers[i][letter]
                if '#' in self.pointers[i]:
                    found = True
            else:
                self.pointers[i] = None
        self.pointers = [pointer for pointer in self.pointers if pointer]

        if letter in self.trie:
            pointer = self.trie[letter]
            if '#' in pointer:
                found = True
            self.pointers.append(pointer)
        else:
            self.pointers = []

        return found

class StreamChecker2:

    def __init__(self, words: List[str]):
        # self.pointers = []
        self.cur = {}
        self.trie = {}
        for word in words:
            node = self.trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node[ch]['parent'] = node
                node = node[ch]
            node['#'] = '#'
        print(self.trie)

    def query(self, letter: str) -> bool:
        if self.cur == {}:
            if letter in self.trie:
                self.cur = self.trie[letter]
                if '#' in self.cur:
                    return True
            else:
                return False

        while self.cur and letter not in self.cur:
            self.cur = self.cur.get('parent', {})

        if self.cur == {}:
            return False
        else:
            self.cur = self.cur[letter]
            if '#' in self.cur:
                return True

        return False

import collections

class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = collections.deque([])
        self.trie = {}
        for word in words:
            node = self.trie
            for ch in word[::-1]:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = '#'
        # print(self.trie)

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for ch in self.stream:
            if '#' in node:
                return True
            if ch not in node:
                return False
            node = node[ch]
        return '#' in node



        # stream = a x y z
        #z y x a
        # words = ["abc", "xyz"] -> reverse ["cab","zyx"]

        # if letter in self.cur:
        #     self.cur = self.cur[letter]
        #     if '#' in self.cur:
        #         return True
        # else:
        #     if letter in self.trie:
        #         self.cur = self.trie[letter]
        #         if '#' in self.cur:
        #             return True
        # return False

if __name__ == '__main__':
    s = StreamChecker(["ab", "ba", "aaab", "abab", "baa"])

    queries = [["a"], ["a"], ["a"], ["a"], ["a"], ["b"], ["a"], ["b"], ["a"], ["b"], ["b"],
     ["b"], ["a"], ["b"], ["a"], ["b"], ["b"], ["b"], ["b"], ["a"], ["b"], ["a"], ["b"], ["a"], ["a"], ["a"], ["b"],
     ["a"], ["a"], ["a"]]

    # s = StreamChecker(["abaa","abaab","aabbb","bab","ab"])
    #
    # queries = [["a"],["a"],["b"],["b"],["b"],["a"],["a"],["b"],["b"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["b"],["b"],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["a"],["b"],["b"],["b"],["a"],["b"],["a"]]

    # s = StreamChecker(["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab","aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"])
    #
    # queries = [["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"],["a"]]


    for i, q in enumerate(queries):
        s.query(q[0])