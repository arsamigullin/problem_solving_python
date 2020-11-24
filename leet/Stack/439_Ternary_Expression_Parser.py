
class Solution:
#
# since the given expression is valid and only consists of digits 0-9, ?, :, T and F (T and F represent True and False respectively).
# we can use expression
    def parseTernary(self, expression):
        def dfs(it):
            first, second = next(it), next(it, None)

            if not second or second == ':':
                return first
            else:
                T, F = dfs(it), dfs(it)
                return T if first == 'T' else F

        return dfs(iter(expression))

if __name__ == '__main__':
    s = Solution()
    s.parseTernary("F?1:T?4:5")