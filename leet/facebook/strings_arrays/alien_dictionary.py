import collections

# these both solutions are the same
# we have ind that contains count of being referenced from parent node
# The nodes with count 0 never were referenced and they are parents
# once the graph is constructed we do dfs and decrease count from ind when traversing the child
# we add to the answer the parent node or the child node with count is equal 0 in ind
from typing import List


class Solution:
    def alienOrder(self, words: list) -> str:
        # Base case
        if not words:
            return ''

        # Create letters
        letters = list(set(''.join(words)))
        # this contains the count the letter is being referenced from parent node
        ind = {char: 0 for char in letters}

        # Create Graph
        # Let's do defaultdict(list) and also populate in-degrees
        graph = collections.defaultdict(list)

        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]
            for j in range(min(len(word1), len(word2))):
                char1 = word1[j]
                char2 = word2[j]
                if char1 != char2:
                    # Populate graph and in-degree dicts
                    if char2 not in graph[char1]:
                        graph[char1].append(char2)
                        ind[char2] += 1 # do not forget to decrease the count of being referenced from parent (char1) node
                    break

        # Now do topological sort
        q = collections.deque()
        for key, val in ind.items():
            if val == 0:
                q.append(key)

        ans = ''
        while q:
            char = q.popleft()
            ans += char
            for letter in graph[char]:
                ind[letter] -= 1
                if ind[letter] == 0: # since no parents that has reference to the ind[letter], hence this child becomes
                    # parent
                    q.append(letter)

        return ans if len(ans) == len(letters) else ''

import collections


class SolutionOpt:
    def alienOrder(self, words):
        pre, suc = collections.defaultdict(set), collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b) # children
                    pre[b].add(a) # parents
                    break
        chars = set(''.join(words))
        free = chars - set(pre) # get the parents that were not referenced
        order = ''
        # do DFS
        while free:
            a = free.pop()
            order += a
            for b in suc[a]:
                pre[b].discard(a)
                if not pre[b]: # since no parents that has reference to the ind[letter], hence this child becomes
                    # parent
                    free.add(b)
        return order * (set(order) == chars)


class SolutionDFS:
    def alienOrder(self, words: List[str]) -> str:

        n = len(words)
        letters = list(set(''.join(words)))
        # this contains the count the letter is being referenced from parent node
        graph = {char: set() for char in letters}
        for i in range(n - 1):
            word1 = words[i]
            word2 = words[i + 1]

            for j in range(min(len(word1), len(word2))):
                ch1 = word1[j]
                ch2 = word2[j]
                if ch1 != ch2:
                    graph[ch1].add(ch2)
                    break
            else:
                if len(word1) > len(word2):
                    return ""

        topsort = []
        visited = collections.defaultdict(int)
        UNVISITED, VISITING, VISITED = 0, 1, 2

        def dfs(node):
            if node not in visited:
                visited[node] = VISITING
                for child in graph[node]:
                    if not dfs(child):
                        return False
                visited[node] = VISITED
                topsort.append(node)
                return True
            else:
                return visited[node] == VISITED

        hasCycle = False
        for node in graph:
            if node not in visited:
                if not dfs(node):
                    hasCycle = True
                    break

        return ''.join(reversed(topsort)) if not hasCycle else ""

if __name__ == "__main__":
    s = SolutionOpt()
    s.alienOrder(["vlxpwiqbsg","cpwqwqcd"])
    s.alienOrder([
  "wrt",
  "wrqq",
  "erqq",
  "ettt",
  "ettq",
  "rftq"
])