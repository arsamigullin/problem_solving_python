import collections
from typing import List
# graph
#

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = collections.defaultdict(list)
        for p, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l >= 0:
                graph[p].append(l)
            if r >= 0:
                graph[p].append(r)
            if len(graph[p]) > 2:
                return False
        # print(graph)
        in_degree = [0] * n
        for i in graph:
            for j in graph[i]:
                in_degree[j] += 1
        start = -1
        for i, val in enumerate(in_degree):
            if val == 0:
                if start >= 0:
                    return False
                start = i

        if start == -1:
            return False
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for child in graph[node]:
                if child in visited:
                    return False
                if not dfs(child):
                    return False
            return True

        return dfs(start) and len(visited) == n

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
      for k in range(0, n):
        stack = [k]
        v = set()
        while stack:
          i = stack.pop()
          v.add(i)

          l = leftChild[i]
          r = rightChild[i]

          if l != -1:
            # if lef is already someone's child
            if l in v:
              return False
            stack.append(l)
          if r != -1:
            # if right is already someone's child
            if r in v:
              return False
            stack.append(r)

        if len(v) == n:
          return True
      return False

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = collections.defaultdict(list)
        in_degree = set(range(n))
        for p, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l >=0:
                in_degree.discard(l)
                graph[p].append(l)
            if r>=0:
                in_degree.discard(r)
                graph[p].append(r)
            if len(graph[p])>2:
                return False
        #print(in_degree)
        if len(in_degree) != 1:
            return False
        visited = set()

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for child in graph[node]:
                if  child in visited:
                    return False
                if not dfs(child):
                    return False
            return True

        return dfs(in_degree.pop()) and len(visited) == n


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = collections.defaultdict(list)
        in_degree = set(range(n))
        for p, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l >= 0:
                in_degree.discard(l)
                graph[p].append(l)
            if r >= 0:
                in_degree.discard(r)
                graph[p].append(r)
            if len(graph[p]) > 2:
                return False
        # print(in_degree)
        if len(in_degree) != 1:
            return False
        visited = set()

        q = collections.deque([in_degree.pop()])
        while q:
            node = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for child in graph[node]:
                if child in visited:
                    return False
                q.append(child)

        def dfs(node):
            if node in visited:
                return False
            visited.add(node)
            for child in graph[node]:
                if not dfs(child):
                    return False
            return True

        return len(visited) == n