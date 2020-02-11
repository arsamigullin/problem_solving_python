# this solution is slow but looks right
# we declared TrieNode. It store list of TrieNodes inside of length 26
class TrieNode:
    def __init__(self):
        self.links = [None] * 26
        self.end = False

    def get(self, char):
        return self.links[ord(char) - ord('a')]

    def contains(self, char):
        return self.links[ord(char) - ord('a')] != None

    def put(self, char, node):
        index = ord(char) - ord('a')
        self.links[index] = node

    def is_end(self):
        return self.end

    def set_end(self):
        self.end = True


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if not node.contains(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

    def __search_prefix(self, word):
        node = self.root
        for ch in word:
            if node.contains(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.__search_prefix(word)
        return node is not None and node.is_end()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.__search_prefix(prefix)
        return node is not None

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# this solution is much faster but underneath it uses dict
class TrieDict:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode = self.root
        for c in word:
            if c not in currNode:
                currNode[c] = dict()
            currNode = currNode[c]
        # this placeholder denotes the end of a string
        # consider these two  words abcc and abccd
        # after inserting the words to the trie we have
        # {'a': {'b': {'c': {'c': {'#': '#'}}}}}
        # {'a': {'b': {'c': {'c': {'#': '#', 'd': {'#': '#'}}}}}}
        # when searching the word after reaching the latest letter in word
        # we also check if the '#' among children of the latest letter
        # so the '#' allows us to say if the whole word (not prefix) is in the Trie
        currNode['#'] = '#'
        print(self.root)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode = self.root
        for c in word:
            if c not in currNode:
                return False
            currNode = currNode[c]
        return '#' in currNode

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode = self.root
        for c in prefix:
            if c not in currNode:
                return False
            currNode = currNode[c]
        return True

if __name__ == "__main__":
    s = TrieDict()
    s.insert("abcc")
    s.insert("abccd")
