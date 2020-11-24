from operator import mul, floordiv, sub, add
class Solution:
    def calculate(self, s: str) -> int:
        d = {"*":mul,"+":add,"-":sub,"/":floordiv }
        stack = []
        s = s.replace(" ", "")
        prev_oper = ""
        i = 0
        while i < len(s):
            j = i
            while i<len(s) and s[i].isnumeric():
                i+=1
            if i!=j:
                if prev_oper in ("*", "/"):
                    last = stack[-1]
                    sign = 1 if last > 0 else -1
                    stack[-1] = sign * d[prev_oper](abs(last),int(s[j:i]))
                else:
                    stack.append(int(prev_oper+s[j:i]))
            else:
                prev_oper = s[i]
                i+=1
        return sum(stack)