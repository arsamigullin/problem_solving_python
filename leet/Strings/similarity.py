import collections


class Solution:
    def numSimilarGroups(self, strs) -> int:
        strs = set(strs)

        def get_children(word):
            n = len(word)
            for i in range(n):
                for j in range(i + 1, n):
                    word[i], word[j] = word[j], word[i]
                    w = ''.join(word)
                    if w in strs:
                        yield w
                    word[i], word[j] = word[j], word[i]
            return []

        count = 0

        q = collections.deque([strs.pop()])
        while len(strs) > 0:
            while q and len(strs) > 0:
                word = q.popleft()
                children = set()
                for child in get_children(list(word)):
                    children.add(child)
                    q.append(child)
                strs ^= children
            count += 1
        return count

if __name__ == '__main__':
    s =Solution()
    s.numSimilarGroups(["tars","rats","arts","star"])