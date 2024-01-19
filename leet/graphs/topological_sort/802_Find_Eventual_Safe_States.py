class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        safeNodes = set()
        state = [0] * len(graph)

        def dfs(node):
            if state[node] == 0:
                state[node] = 1
                hasSavfeNodes = True
                for ch in graph[node]:
                    if not dfs(ch):
                        hasSavfeNodes = False
                        break
                if hasSavfeNodes:
                    safeNodes.add(node)
                state[node] = 2
                return hasSavfeNodes
            else:
                return state[node] == 2 and node in safeNodes

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res

    def eventualSafeNodes1(self, graph: List[List[int]]) -> List[int]:

        safeNodes = set()
        indegree = collections.defaultdict(int)
        n = len(graph)
        adj = collections.defaultdict(list)
        for i in range(n):
            for ch in graph[i]:
                indegree.setdefault(ch, 0)
                adj[ch].append(i)
                indegree[i] += 1

        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        state = [False] * n
        while q:
            node = q.popleft()
            state[node] = True
            for ch in adj[node]:
                indegree[ch] -= 1
                if indegree[ch] == 0:
                    q.append(ch)

        safe = []
        for i in range(n):
            if state[i]:
                safe.append(i)
        return safe