# https://leetcode.com/problems/k-similar-strings/discuss/269517/Python-Graph-BFS

# this is BFS
class Solution1:
    def kSimilarity(self, A: str, B: str) -> int:
        def nei(x):
            # aabc
            # abca
            i = 0
            while x[i] == B[i]:
                i+=1
            # in this loop we try to find the first match
            for j in range(i+1, len(x)):
                # if x[j] == B[i]:
                if x[j] == B[i] and x[j] != B[j]:
                    # basically this is swapping of x[i] and x[j] chars
                    yield x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:]
        q, seen = [(A,0)], {A}
        for x, d in q:
            if x == B:
                return d
            for y in nei(x):
                if y not in seen:
                    seen.add(y)
                    q.append((y,d+1))


class Solution2:
    def kSimilarity(self, s1: str, s2: str) -> int:
        q, seen = [s1], {s1}
        ans = 0
        while q:
            nxt = []
            for s in q:
                if s == s2:
                    return ans
                for i in range(len(s)):
                    if s[i] != s2[i]:
                        for j in range(i + 1, len(s)):
                            if s[j] == s2[i] and s[j] != s2[j]:
                                t = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                                if t not in seen:
                                    nxt.append(t)
                                    seen.add(t)
                        break
            ans += 1
            q = nxt
            print(q)


from collections import defaultdict
from collections import Counter
import itertools as it


class Solution3:
    def kSimilarity(self, s1: str, s2: str) -> int:

        # Construct graph from the strings:
        adj = defaultdict(Counter)
        for c1, c2 in zip(s1, s2):
            adj[c1][c2] += 1

        for c in adj:
            adj[c][c] = 0

        # Simplify graph by removing single swaps:
        k = 0
        for a, b in it.combinations(adj, 2):
            if adj[a][b] and adj[b][a]:
                m = min(adj[a][b], adj[b][a])
                adj[a][b] -= m
                adj[b][a] -= m
                k += m

        # Re-structure graph:
        adj = defaultdict(list,
                          {a: "".join(b * r for b, r in c.items())
                           for a, c in adj.items()})

        # Using DFS count number of tree-edges + forward-edges = min swaps:
        closed, opened = set(), set()

        def dfs(u):
            if u in closed or u in opened:
                return u in closed

            opened.add(u)
            result = sum(dfs(v) for v in adj[u]) + 1
            opened.remove(u)
            closed.add(u)

            return result

        return sum(dfs(w) - 1 for w in set(s1) if w not in closed) + k


if __name__ == '__main__':
    s = Solution1()
    s.kSimilarity("aabc", "abca")
