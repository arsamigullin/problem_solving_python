class Solution:
    def generateParenthesis(self, n: int) -> list:

        res = []

        def generate(S='', left=0, right=0):
            if len(S) == 2 * n:
                res.append(S)
                return
            if left < n:
                generate(S + '(', left + 1, right)
            # note: this is important here
            # right should be less than left
            if right < left:
                generate(S + ')', left, right + 1)

        generate()
        return res

if __name__ == "__main__":
    s = Solution()
    s.generateParenthesis(3)