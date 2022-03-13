import collections
from typing import List


class TrieNode():
    def __init__(self, name=None, tp='FOLDER'):
        self.name = name
        self.children = collections.defaultdict()
        self.cont = []
        self.type = tp


class FileSystem:

    def __init__(self):
        self.trie = TrieNode('/', '/')

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return sorted(t.name for t in self.trie.children.values())
        names = path.split('/')
        node = self.trie
        for path in names[1:]:
            node = node.children[path]
        if node.type == 'FILE':
            return [node.name]
        return sorted(t.name for t in node.children.values())

    def mkdir(self, path: str) -> None:
        names = path.split('/')
        node = self.trie
        whole = []
        for path in names[1:]:
            whole.append('' if path == '/' else path)
            if path not in node.children:
                node.children[path] = TrieNode(path)
            node = node.children[path]

    def addContentToFile(self, filePath: str, content: str) -> None:
        names = filePath.split('/')
        node = self.trie
        for path in names[1:]:
            if path not in node.children:
                node.children[path] = TrieNode(path)
            node = node.children[path]
        node.cont.append(content)
        node.type = 'FILE'

    def readContentFromFile(self, filePath: str) -> str:
        names = filePath.split('/')
        node = self.trie
        for path in names[1:]:
            node = node.children[path]
        return ''.join(node.cont)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)