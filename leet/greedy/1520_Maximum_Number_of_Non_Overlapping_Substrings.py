from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        entries = {c: [s.index(c), s.rindex(c)+1] for c in set(s)}
        # find all the correct boundries
        pairs = []
        for c in set(s):
            l = i = entries[c][0]
            r = j = entries[c][1]
            while True:
                t = set(s[i:j])
                # this just extends the range if inside of l and r there are chars that have lower or greater l and r
                for k in t:
                    i = min(i, entries[k][0])
                    j = max(j, entries[k][1])
                if (i, j) == (l, r):
                    break
                l, r = i, j
            pairs.append([l, r])

        # greedily find the optimal solution
        # similar to find the maximum number of meetings
        pairs.sort(key=lambda x: x[1])
        res, last = [], 0
        for b, e in pairs:
            if b >= last:
                res.append(s[b:e])
                last = e
        return res

if __name__ == '__main__':
    s = Solution()
    s.maxNumOfSubstrings("adefaddaccc")
    s.maxNumOfSubstrings("abann")
    s.maxNumOfSubstrings("ababca")