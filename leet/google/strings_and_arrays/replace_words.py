import collections
from functools import reduce
from typing import List


class SolutionMy:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = {}
        for word in dict:
            node = trie
            for ch in word:
                if ch in node:
                    node = node[ch]
                else:
                    node[ch] = {}
                    node = node[ch]
            node['#'] = '#'

        words = sentence.split()
        print(words)
        res = []

        for word in words:
            node = trie
            cur = ''
            for ch in word + '#':
                if '#' in node:
                    res.append(cur)
                    break
                if ch in node:
                    cur += ch
                    node = node[ch]
                else:
                    res.append(word)
                    break

        return ' '.join(res)



class SolutionHaspMap:
    def replaceWords(self, roots, sentence):
        rootset = set(roots)

        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

class SolutionTrie(object):
    def replaceWords(self, roots, sentence):
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur: break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))

if __name__ == '__main__':
    s = SolutionTrie()
    s.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")