from typing import List


class Solution:
  def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbidden = set(forbidden)
        n = len(word)
        left = 0
        res = 0
        for i in range(n):
            for j in range(max(i-9, left), i+1):
                if word[j:i+1] in forbidden:
                    left = j + 1
            res = max(res, i - left + 1)
        return res


class Solution1:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        forbiddenSet = set(forbidden)
        ans = 0
        r = len(word) - 1  # rightmost index of the valid substring

        for l in range(len(word) - 1, -1, -1):
            for end in range(l, min(l + 10, r + 1)):
                if word[l:end + 1] in forbiddenSet:
                    r = end - 1
                    break
            ans = max(ans, r - l + 1)

        return ans


if __name__ == '__main__':
    s = Solution()
    s.longestValidSubstring("leetcode", ["de","le","e"])
    s.longestValidSubstring("cbcbcbcbcbcbcbcbcbcbcbcbccbcbcbcbcb", ["a"])
    s.longestValidSubstring("cbaaaabc", ["aaa", "cb"])
