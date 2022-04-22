# similar to
# 1597_Build_Binary_Expression_Tree_From_Infix_Expression.py
import operator

pr = {'+': 2, '-': 2, ')': 3, '(': 4}
ops = {'+': operator.add, '-': operator.sub}


class Solution(object):
    def apply(self, numSt, opSt):
        right = numSt.pop()
        left = numSt.pop()
        return ops[opSt.pop()](left, right)

    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        numSt, opSt = [], []
        i = 0
        while (i < len(s)):
            c = s[i]
            if (i == 0 and c == '-' and s[i + 1].isnumeric()) or s[i].isnumeric():
                j = i + 1 if c == '-' else i
                while j < len(s) and s[j].isnumeric():
                    j += 1
                numSt.append(int(s[i:j]))
                i = j
            else:
                if c in '(':
                    opSt.append('(')
                else:
                    while (len(opSt) > 0 and pr[c] >= pr[opSt[-1]]):
                        numSt.append(self.apply(numSt, opSt))
                    if c == ')':
                        opSt.pop()  # Now what remains is the closing bracket ')'
                    else:
                        opSt.append(c)
                i += 1
        # print(numSt)
        while (len(opSt) > 0 and len(numSt) > 1):
            numSt.append(self.apply(numSt, opSt))
        sign = 1 if len(opSt) == 0 else -1
        return sign * numSt.pop()


if __name__ == '__main__':
    s = Solution()
    s.calculate("(1+(4+5+2)-3)+(6+8)")
