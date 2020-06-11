# this is my solution
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = dict()
            node = node[ch]
        node['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        # print(self.root)
        node = self.root

        def find(w, i, n):
            if i == len(w):
                return '#' in n
            if w[i] == '.':
                for k, v in n.items():
                    if k == '#':
                        continue
                    if find(w, i + 1, v):
                        return True
            else:
                if w[i] not in n:
                    return False
                return find(w, i + 1, n[w[i]])
            return False

        return find(word, 0, node)

# this is another solution
class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[None] = None

    def search(self, word):
        def find(word, node):
            if not word:
                return None in node
            char, word = word[0], word[1:]
            if char != '.':
                return char in node and find(word, node[char])
            return any(find(word, kid) for kid in node.values() if kid)

        return find(word, self.root)