class Solution:
    def addOperators(self, num: str, target: int) -> str:
        operators = ['*','-','+']
        def backtrack(i, s):
            group = i + 1
            while group < len(s[i:]):
                for oper in operators:
                    backtrack(group,s[:group] + oper + s[group:])

        backtrack(0,num)

if __name__ == "__main__":
    s=Solution()
    s.addOperators("12345", 25)