class Solution:
    def minAddToMakeValid(self, S: str) -> int:

        balance = 0
        cnt = 0
        for ch in S:
            if ch == ')':
                balance -= 1
                if balance < 0:
                    cnt += 1
            else:
                if balance < 0:
                    balance = 0
                balance += 1
        return cnt + max(0, balance)

class Solution(object):
    def minAddToMakeValid(self, S):
        ans = bal = 0
        for symbol in S:
            bal += 1 if symbol == '(' else -1
            # It is guaranteed bal >= -1
            if bal == -1:
                ans += 1
                bal += 1
        return ans + bal