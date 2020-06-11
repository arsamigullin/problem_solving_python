import collections
from typing import List


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            node = self.trie
            for ch in word:
                if ch not in node:
                    node[ch] = {}
                node = node[ch]
            node['#'] = '-'
        # print(self.trie)

    def find(self, i, count, node, word):
        if count > 1:
            return False
        if i >= len(word):
            return '#' in node and count == 1
        ch = word[i]
        for key in node:
            if key == '#':
                continue
            cnt = ch != key
            if self.find(i + 1, count + cnt, node[key], word):
                return True
        return False

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """

        return self.find(0, 0, self.trie, word)


class MagicDictionary(object):
    def __init__(self):
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):

        for candidate in self.buckets[len(word)]:
            tot = 0
            for a, b in zip(word, candidate):
                tot += a != b
            if tot == 1:
                return True
        return False
        # return any(sum(a!=b for a,b in zip(word, candidate)) == 1
        #            for candidate in self.buckets[len(word)])

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictionary = None
        self.word = None

    def pattern(self, word):
        for idx in range(len(word)):
            yield word[:idx] + '*' + word[idx + 1:]

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.word = set(dict)
        self.dictionary = collections.Counter(p for word in dict
                                              for p in self.pattern(word))

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return any(self.dictionary[p] > 1 or
                   (self.dictionary[p] == 1 and word not in self.word)
                   for p in self.pattern(word))
