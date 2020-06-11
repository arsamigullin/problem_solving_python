class Solution:
    def backtracking(self, s, r):
        ans = []
        def helper(i, combs):
            if len(combs) == r:
                ans.append(combs[:])
                return
            for j in range(i, len(s)):
                combs.append(s[j])
                helper(j+1, combs)
                combs.pop()

        helper(0,[])
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.backtracking("ABCDE", 3))

