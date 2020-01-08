# set is much faster
class MySolution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        to_remove = set()
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    to_remove.add(i)
        #print(to_remove)
        to_remove = to_remove.union(set(stack))

        return ''.join([s[i] for i in range(len(s)) if i not in to_remove])

# this solution is faster
# we replace with empty in place
# if after first iteration the balance is greater than 0
# we have to remove all "("
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        arr = list(s)
        balance = 0
        for i in range(len(arr)):
            if arr[i] == "(":
                balance += 1
            elif arr[i] == ")":
                if balance == 0:
                    arr[i] = ""
                else:
                    balance -= 1
        i = len(arr) - 1
        while balance > 0 and i >= 0:
            if arr[i] == "(":
                arr[i] = ""
                balance -= 1
            i -= 1
        return "".join(arr)