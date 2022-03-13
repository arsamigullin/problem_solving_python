import collections


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        i, j = 0, 0
        visited = collections.defaultdict(int)
        max_len = 1
        while j < n:
            if visited[s[j]] == 1:
                visited[s[j]] += 1
                max_len = max(max_len, len(visited))
                while visited[s[j]] != 1:
                    visited[s[i]] -= 1
                    if visited[s[i]] == 0:
                        visited.pop(s[i])
                    i += 1
            else:
                visited[s[j]] += 1
            j += 1

        return max(max_len, len(visited))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        i, j = -1, 0
        max_len = 0
        mp = collections.defaultdict(int)
        for j in range(n):
            ch = s[j]
            if ch in mp:
                # we use this max to cover the case when the pointer i is greater than index under ch
                # for example, abba, when pointer i at the second a, mp[a] is 0
                # but i is already set to the index 2, hence we cannot set it less than 2
                i = max(mp[ch],i)
            max_len = max(max_len, j-i)
            mp[ch]=j
        return max_len

if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring("abcabcbb")