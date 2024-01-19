# O(K + M^N * M * N)
# M is 26
# N is word length (up to 26)
# K is len of wordList
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        chars = set(''.join(wordList))
        visited = {beginWord}
        q = deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for ch in chars:
                for i in range(len(word)):
                    if ch != word[i]:
                        newWord = word[:i] + ch + word[i+1:]
                        if newWord in wordList and newWord not in visited:
                            q.append((newWord, steps + 1))
                            visited.add(newWord)
        return 0

# O(M^2 * N)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        graph = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                node = word[:i] + '*' + word[i + 1:]
                graph[node].append(word)

        visited = {beginWord}
        q = deque([(beginWord, 1)])
        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                node = word[:i] + '*' + word[i + 1:]
                for child in graph[node]:
                    if child not in visited:
                        q.append((child, steps + 1))
                        visited.add(child)
        return 0
