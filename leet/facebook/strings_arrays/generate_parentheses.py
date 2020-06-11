from typing import List


class Solution1:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def get(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                get(s + '(', left + 1, right)
            if right < left:
                get(s + ')', left, right + 1)

        get('', 0, 0)

        return res


class Solution2(object):
    def generateParenthesis(self, N):
        if N == 0: return ['']
        ans = []
        for c in range(N):
            for left in self.generateParenthesis(c):
                for right in self.generateParenthesis(N-1-c):
                    ans.append(f'({left}){right}')
        return ans

if __name__ == "__main__":
    s = Solution2()
    s.generateParenthesis(3)