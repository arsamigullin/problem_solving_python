import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(beginWord)
        options = collections.defaultdict(list)

        # this is graph
        for w in wordList:
            for i in range(n):
                options[w[:i] + '*' + w[i + 1:]].append(w)

        visited = set()
        q = collections.deque([(beginWord, 1)])
        while q:
            w, level = q.popleft()
            if w in visited:
                continue
            if w == endWord:
                return level
            visited.add(w)
            for i in range(n):
                for nei in options[w[:i] + '*' + w[i + 1:]]:
                    if nei not in visited:
                        q.append((nei, level + 1))
        return 0


class Solution:
    # Given a graph G(V,E) and a distinguished source vertex s, breadth-ﬁrst
    # search systematically explores the edges of G to “discover” every vertex that is
    # reachable from s. It computes the distance (smallest number of edges) from s
    # to each reachable vertex (Cormen, 594)
    #
    # think about this task in terms of graph
    # 1. We need to find the shortest path from beginWord to endWord
    # Before we proceed we need to collect all the possible words with one missing letter
    # this word with a placeholder in it (let say the placeholder will be "*")
    # will contain all the words with one letter difference
    # for example, in word hit we put placeholder instead of i and we got h*t
    # under this word the words hot, hyt will fall
    # 2. After collecting these words we will start BFS initializing queue with (beginWord, 1)
    # where 1 is level. Replacing one of the letters of popped item with "*" (intermediate_word)
    # we will explore all the words that fall under this intermediate_word.
    # Once the word equals endWord return level
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        l = len(beginWord)
        combo_words = collections.defaultdict(list)
        #1
        for w in wordList:
            for i in range(l):
                combo_words[w[:i] + "*" + w[i+1:]].append(w)
        visited = {beginWord: True}
        queue = collections.deque([(beginWord,1)])
        while len(queue) > 0:
            word, level = queue.popleft()
            for i in range(l):
                intermediate_word = word[:i] + "*" + word[i + 1:]
                for w in combo_words[intermediate_word]:
                    if w == endWord:
                        return level + 1
                    if w not in visited:
                        visited[w] = True
                        queue.append((w, level + 1))
            #combo_words[intermediate_word] = []

        return 0



if __name__ == "__main__":
    s = Solution()
    s.ladderLength("hit", "cog", ["lot","hot","dot","cog","dog","log"])
