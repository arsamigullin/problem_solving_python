import collections


class Solution:
    def maxPower(self, s: str) -> int:
        count = 0
        start = 0
        end = 0
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                end+=1
            else:
                count = max(count, end - start + 1)
                start = i
                end = i
        print(count)

if __name__ == '__main__':
    s = Solution()
    s.maxPower('leetcode')Minimum Height Trees