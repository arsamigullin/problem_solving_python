from collections import Counter

# this is the same as below
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        def helper(s):
            c = Counter(s)
            for i, ch in enumerate(s):
                if c[ch] < k:
                    subs1 = helper(s[:i])
                    subs2 = helper(s[i + 1:])
                    break
            else:
                return len(s)

            return max(subs1, subs2)

        return helper(s)

# this is same as above
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

# sliding window
class Solution1:
    def longestSubstring(self, s, k):
        count = 0
        for i in range(1, 27):
            count = max(count, self.helper(s, k, i))
        return count

    def helper(self, s, k, numUniqueTarget):
        start = end = numUnique = numNoLessThanK = count = 0
        chMap = [0] * 128

        while end < len(s):
            if chMap[ord(s[end])] == 0: numUnique += 1
            chMap[ord(s[end])] += 1
            if chMap[ord(s[end])] == k: numNoLessThanK += 1
            end += 1

            while numUnique > numUniqueTarget:
                if chMap[ord(s[start])] == k: numNoLessThanK -= 1
                chMap[ord(s[start])] -= 1
                if chMap[ord(s[start])] == 0: numUnique -= 1
                start += 1

            if numUnique == numNoLessThanK: count = max(count, end - start)

        return count


class Solution2:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k or k == 0 or not s:
            return 0
        longest = 0
        sCount = Counter(s)
        split_index = 0
        while split_index < len(s) and k <= sCount[s[split_index]]:
            split_index += 1
        if split_index == len(s):
            return len(s)

        left = self.longestSubstring(s[:split_index], k)
        while split_index < len(s) and sCount[s[split_index]] < k:
            split_index += 1
        right = self.longestSubstring(s[split_index:], k)
        return max(left, right)


import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)



class SolutionWrong:
    def longestSubstring(self, s: str, k: int) -> int:
        if k > len(s):
            return 0
        d = collections.defaultdict(int)
        c = collections.Counter(s)
        print(c)
        d[s[0]] = 1
        cnt = 0
        j = 1
        for i in range(1, len(s)):
            d[s[i]] += 1
            if s[i - 1] == s[i]:
                j += 1
            else:
                j = 1
                if d[s[i - 1]] == c[s[i - 1]] and c[s[i - 1]] < k:
                    print(d)
                    d = collections.defaultdict(int)
                    d[s[i]] = 1

            if all(d[key] >= k for key in d):
                # print(d)
                cnt = max(cnt, sum(d.values()))
                print(cnt)
            if j >= k:
                cnt = max(cnt, j)

        print(d)
        if all(d[key] >= k for key in d):
            cnt = max(cnt, sum(d.values()))
        return cnt

if __name__ == '__main__':
    s = Solution()
    s.longestSubstring("zzzzzzzzzzaaaaaaaaabbbbbbbbhbhbhbhbhbhbhicbcbcibcbccccccccccbbbbbbbbaaaaaaaaafffaahhhhhiaahiiiiiiiiifeeeeeeeeee", 10)