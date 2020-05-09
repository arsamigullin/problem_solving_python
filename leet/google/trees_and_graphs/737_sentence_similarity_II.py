from typing import List

# NlogP + P
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        parent = {}
        size = {}

        def find(p):
            parent.setdefault(p, p)
            size.setdefault(p, 1)
            root = p
            while root != parent[root]:
                root = parent[root]
            while root != p:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def union(p, q):
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            if size[rootP] > size[rootQ]:
                parent[rootQ] = rootP
                size[rootP] += size[rootQ]
            else:
                parent[rootP] = rootQ
                size[rootQ] += size[rootP]

        for a, b in pairs:
            if find(a) != find(b):
                union(a, b)
        for u, v in zip(words1, words2):
            if u == v:
                continue
            if find(u) != find(v):
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    s.areSentencesSimilarTwo(["a","very","delicious","meal"],
["one","really","delicious","dinner"],
[["great","good"],["extraordinary","good"],["well","good"],["wonderful","good"],["excellent","good"],["fine","good"],["nice","good"],
 ["any","one"],["some","one"],["unique","one"],["the","one"],["an","one"],["single","one"],["a","one"],["truck","car"],
 ["wagon","car"],["automobile","car"],["auto","car"],["vehicle","car"],["entertain","have"],["drink","have"],
 ["eat","have"],["take","have"],["fruits","meal"],["brunch","meal"],["breakfast","meal"],["food","meal"],
 ["dinner","meal"],["super","meal"],["lunch","meal"],["possess","own"],["keep","own"],["have","own"],
 ["extremely","very"],["actually","very"],["really","very"],["super","very"]])