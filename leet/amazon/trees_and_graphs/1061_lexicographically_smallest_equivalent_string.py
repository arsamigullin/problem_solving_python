# union_find
import collections


class Solution1:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:

        all_letters = set(A + B)
        parent = {v: v for v in all_letters}
        size = {v: 1 for v in all_letters}
        N = len(parent)

        def find(p):
            root = p
            while root != parent[p]:
                root = parent[p]
            while root != p:
                newp = parent[p]
                parent[p] = root
                p = newp
            return root

        def find(p):
            root = p
            while root!=parent[root]:
                root = parent[root]
            while p!=root:
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

        for a, b in zip(A, B):
            if find(a) != find(b):
                union(a, b)
        d = collections.defaultdict(set)

        print(parent)
        for k in all_letters:
            d[find(k)].add(k)

        for k in d:
            d[k] = sorted(d[k])

        print(d)
        return ''.join([ch if ch not in parent else d[find(ch)][0] for ch in S])


class Solution3:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        uf = {}

        def find(i):
            uf.setdefault(i, i)
            if uf[i] != i:
                uf[i] = find(uf[i])
            return uf[i]

        def union(i, j):
            # we assign the smallest parent of two nodes(i,j) to a greater parent of two nodes(i,j)
            # the benefit of that is the each node will pe pointing to lexicogrphically smallest value
            x, y = find(i), find(j)
            uf[max(x, y)] = min(x, y)

        for a, b in zip(A, B):
            union(a, b)
                # print(uf)
        return "".join(find(c) for c in S)


        # return ''.join([d[ch]])
if __name__ == '__main__':
    s = Solution2()
    s.smallestEquivalentString("parker", "morris", "parser")
    s.smallestEquivalentString("dfeffdfafbbebbebacbbdfcfdbcacdcbeeffdfebbdebbdafff",
"adcdfabadbeeafeabbadcefcaabdecabfecffbabbfcdfcaaae",
"myickvflcpfyqievitqtwvfpsrxigauvlqdtqhpfugguwfcpqv")








