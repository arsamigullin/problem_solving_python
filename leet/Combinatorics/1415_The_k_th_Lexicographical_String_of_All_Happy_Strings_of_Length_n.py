class SolutionMy:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3 * 2 ** (n - 1)
        if k > total:
            return ""
        res = []

        def helper(perms):
            if len(perms) == n:
                res.append(''.join(perms))
                return
            for ch in ['a', 'b', 'c']:
                if perms and perms[-1] == ch:
                    continue
                perms.append(ch)
                helper(perms)
                if len(res) == k:
                    return
                perms.pop()
        helper([])
        return "" if k > len(res) else res[k - 1]

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        total = 3*2**(n-1)
        if k>total:
            return ""
        chars,last,result = set("abc"),"",[""]*n
        for i in range(n):
            choice = sorted(chars-set(last))
            total //= len(choice)
            last = choice[(k-1)//total]
            result[i],k = last,k%total
        return "".join(result)