from typing import List


class Solution1:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        memo = {}
        #@lru_cache(None)
        def dp(i, open):
            ans = set()
            if open < 0:
                return ans # Invalid -> return 0 result
            if (i, open) not in memo:
                if i == len(s):
                    if open == 0: ans.add("") # Valid -> Return 1 result (empty string)
                    return ans

                if s[i] == '(' or s[i] == ')': # Case 1: Skip s[i]: '(', ')'
                    ans.update(dp(i + 1, open))

                newOpen = open
                if s[i] == '(': newOpen = open + 1
                elif s[i] == ')': newOpen = open - 1
                brackets = dp(i + 1, newOpen)
                for suffix in brackets: # Case 2: Include s[i]: '(', ')' or letter
                    ans.add(s[i] + suffix)
                memo[(i,open)] = ans
            return memo[(i,open)]

        validAnswers = dp(0, 0)
        maxLen = max(map(len, validAnswers))
        return filter(lambda x: len(x) == maxLen, validAnswers)


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = set()
        n = len(s)
        memo = set()

        def dfs(i, balance, brackets):
            if balance < 0:
                return
            if i >= n:
                if balance == 0:
                    result.add(''.join(brackets))
                return
            if s[i].isalpha():
                brackets.append(s[i])
                dfs(i + 1, balance, brackets)
                brackets.pop()
            elif s[i] == '(':
                if balance <= n // 2:
                    brackets.append(s[i])
                    dfs(i + 1, balance + 1, brackets)
                    brackets.pop()
                dfs(i + 1, balance, brackets)
            elif s[i] == ')':
                if balance > 0:
                    brackets.append(s[i])
                    dfs(i + 1, balance - 1, brackets)
                    brackets.pop()
                dfs(i + 1, balance, brackets)

        dfs(0, 0, [])
        result = sorted(result, key=len, reverse=True)
        # print(result)
        max_len = len(result[0])


if __name__ == '__main__':
    s = Solution1()
    s.removeInvalidParentheses("()())()")