from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        entries = {c: [s.index(c), s.rindex(c)+1] for c in set(s)}
        # find all the correct boundries
        pairs = []
        for ch in set(s):
            # initially we have these coordinates
            l = i = entries[ch][0]
            r = j = entries[ch][1]
            # then here we check to see if there is char inside of [i:j] range that have even broader range
            # for examaple s = "acaca" and ch now is 'c' and its range is [1,3]
            # as we can see, between two 'c' there is 'a' with broader range [0,4]
            # so we detected intersection and we update the initial variables (l,r) with i,j
            # and because of that it will stop at some point because all the chars are already explored within [l:r] range
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
    s.maxNumOfSubstrings("abab")
    s.maxNumOfSubstrings("adefaddaccc")
    s.maxNumOfSubstrings("abann")
    s.maxNumOfSubstrings("ababca")