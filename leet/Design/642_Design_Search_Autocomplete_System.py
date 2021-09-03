import collections
from typing import List

#trie trienode

# this is preferrable solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.sortedList = []

    def add_sentence(self, sentence, time):
        cur = self
        for ch in sentence:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.add_sentence_to_sorted_list(sentence, time)

    def add_sentence_to_sorted_list(self, sentence, time):
        for i, (sent, freq) in enumerate(self.sortedList):
            if sent == sentence:
                self.sortedList[i][1] = time
                break
        else:
            self.sortedList.append([sentence, time])

        self.sortedList.sort(key=lambda x: (-x[1], x[0]))
        if len(self.sortedList) > 3:
            self.sortedList.pop()

    def get_hot(self):
        return [sent for sent, _ in self.sortedList]


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.input_chars = []
        self.frequency = collections.defaultdict(int)
        self.trie = TrieNode()
        self.cur = self.trie
        for sentence, time in zip(sentences, times):
            self.frequency[sentence] = time
            self.trie.add_sentence(sentence, time)

    def input(self, c: str) -> List[str]:

        if c == '#':
            new_sentence = ''.join(self.input_chars)
            self.frequency[new_sentence] += 1
            self.trie.add_sentence(new_sentence, self.frequency[new_sentence])
            self.cur = self.trie
            self.input_chars = []
        else:
            self.input_chars.append(c)
            if c in self.cur.children:
                self.cur = self.cur.children[c]
                return self.cur.get_hot()
            else:
                self.cur = TrieNode()
        return []


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentences_by_prefix = collections.defaultdict(collections.defaultdict)
        self.input_chars = []
        self.frequency = collections.defaultdict(int)
        for sentence, time in zip(sentences, times):
            self.frequency[sentence] = time
            self.add_sentence(sentence, time)

    def add_sentence(self, sentence, time):
        for i, ch in enumerate(sentence):
            self.sentences_by_prefix[sentence[:i + 1]][sentence] = time

    def input(self, c: str) -> List[str]:
        result = []
        if c == '#':
            prefix = ''.join(self.input_chars)
            self.frequency[prefix] += 1
            self.add_sentence(prefix, self.frequency[prefix])
            self.input_chars = []
        else:
            self.input_chars.append(c)
            prefix = ''.join(self.input_chars)
            sorted_by_time_then_ascii = sorted(self.sentences_by_prefix[prefix].items(), key=lambda kv: (-kv[1], kv[0]))
            result = [sent for sent, score in sorted_by_time_then_ascii[:3]]
        return result



class AutocompleteSystem1:

    def __init__(self, sentences: List[str], times: List[int]):
        self.count = collections.Counter()
        for s, t in zip(sentences, times):
            self.count[s] = t
        self.curr = ''

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.count[self.curr] += 1
            self.curr, self.res = '', []
            return []

        if not self.curr:
            tmp = [(-n, s) for s, n in self.count.items() if s[0] == c]
            tmp.sort()
            self.res = [s for n, s in tmp]
        else:
            l = len(self.curr)
            self.res = [s for s in self.res if len(s) > l and s[l] == c]

        self.curr += c
        return self.res[:3]
