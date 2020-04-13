import typing
List = typing.List
class Solution1:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        def find(i, exprs, res_so_far=None):
            if i >= len(num):
                if res_so_far == target:
                    result.append(exprs)
                return
            find(i+1, exprs+"*"+num[i], (1 if res_so_far is None else res_so_far)  * int(num[i]))
            find(i+1, exprs+"+"+num[i], (0 if res_so_far is None else res_so_far)  + int(num[i]))
            find(i+1, exprs+"-"+num[i], (0 if res_so_far is None else res_so_far)  - int(num[i]))
            
        find(0,"")
        print(result)

import re
import typing
List = typing.List
class SolutionLoop:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = set()
        d = {}
        def evaluate(expr, reverse=False):
            if expr in d:
                print('It was there')
                return d[expr]
            expr_to_eval = expr
            if reverse:
                expr_to_eval=expr[::-1]
            nums=re.split('\D', expr_to_eval)
            ops = ''.join(re.split('\d', expr_to_eval))

            res = int(nums[0])
            for num, op in zip(nums[1:], ops):
                cast_num = int(num)
                if op == '+':
                    res+=cast_num
                elif op == '-':
                    res-=cast_num
                elif op == '*':
                    res*=cast_num
            d[expr] = res
            print('It was not there')
            return res
                    

        def find(i, exprs):
            if i >= len(num):
                if evaluate(exprs) == target:
                    result.add(''.join(exprs))
                return
            for j in range(i + 1, len(num)+1):
                cur = num[i:j]
                if len(cur) > 1 and cur[0] == '0':
                    return

                for op in ['*','+','-']:
                    if op == '+':
                        upd_exprs = cur if exprs == '' else exprs+"+"+cur
                        evaluate(upd_exprs)
                        find(j, upd_exprs)
                    elif op == '-':
                        upd_exprs = cur if exprs == '' else exprs+"-"+cur
                        evaluate(upd_exprs)
                        find(j, upd_exprs)
                    elif op == '*':
                        upd_exprs = cur if exprs == '' else exprs+"*"+cur
                        evaluate(upd_exprs, True)
                        find(j, upd_exprs)
        find(0,'')
        print(result)
        print(d)


class Solution2:
    def addOperators(self, num: str, target: int) -> List[str]:
        opers = "+-*"
        result = []
        def helper(prev, res, pci, lo, num):
            if not num:
                if pci == len(prev) - 1:
                    if res == target:
                        result.append(''.join(prev))
                else:
                    tot = int(prev[-1])
                    for i in range(len(prev) - 2, pci - 1, -2):
                        n, op = prev[i - 1:i + 1]
                        if op == "*":
                            tot *= (res if pci == i - 1 and pci > 0 else int(n))
                        elif op == "-":
                            tot = (res if pci == i - 1 and pci > 0 else int(n)) - tot
                        else:
                            tot += (res if pci == i - 1 and pci > 0 else int(n))
                    if tot == target:
                        result.append(''.join(prev))
                return


            for i in range(len(num)):
                for op in opers:
                    cur = num[:i + 1]
                    if len(cur) > 1 and cur[0] == '0':
                        continue
                    if not prev:
                        prev.append(cur)
                        helper(prev, res, pci, op, num[i + 1:])
                        prev.pop()
                    else:
                        if lo == "*":
                            tot = cur
                            for i in range(len(prev+[lo]) - 1, pci - 1, -2):
                                num, op = prev[i - 1:i + 1]
                                if op == "*":
                                    tot *= (res if pci == i-1 and pci > 0 else int(num))
                                elif op == "-":
                                    tot =  (res if pci == i-1 and pci > 0 else int(num)) - tot
                                else:
                                    tot += (res if pci == i-1 and pci > 0 else int(num))
                                prev.append(lo)
                                prev.append(cur)
                                helper(prev, tot, len(prev) + len(cur) - 1, op, num[i + 1:])
                                prev.pop()
                                prev.pop()
                        else:
                            prev.append(lo)
                            prev.append(cur)
                            helper(prev, res, pci, op, num[i + 1:])
                            prev.pop()
                            prev.pop()

        helper([], 0, 0, "", num)


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        opers = "+-*"
        result = []

        def helper(number, calc, lo, prev, res):
            if not number:
                if calc == target:
                    result.append(''.join(res[1:]))
                return True
            for i in range(len(number)):
                cur = number[:i + 1]
                if len(cur) > 1 and cur[0] == '0':
                    return
                cur = int(cur)
                if not lo:
                    res.append("+"), res.append(str(cur))
                    shallexit = helper(number[i + 1:], calc + cur, "+", cur, res)
                    res.pop(), res.pop()
                    continue
                for op in opers:
                    if op == "*":
                        lr = len(res)
                        res.append("*"), res.append(str(cur))
                        if lo == "*" or lr == 2:
                            shallexit = helper(number[i + 1:], (calc - prev) + (prev * cur), "*", prev * cur, res)
                        elif lo == "-":
                            shallexit = helper(number[i + 1:], (calc + prev) - (prev * cur), "-", prev * cur, res)
                        elif lo == "+":
                            shallexit = helper(number[i + 1:], (calc - prev) + (prev * cur), "+", prev * cur, res)
                        # else:
                        # helper(number[i + 1:], cur, "*", cur, res)
                    elif op == "+":
                        res.append("+"), res.append(str(cur))
                        shallexit = helper(number[i + 1:], calc + cur, "+", cur, res)
                    elif op == "-":
                        res.append("-"), res.append(str(cur))
                        shallexit = helper(number[i + 1:], calc - cur, "-", cur, res)
                    res.pop(), res.pop()

                if shallexit:
                    return False

        helper(num, 0, "", 0, [])
        print(result)

class SolutionFastest:
    def addOperators(self, num: str, target: int) -> List[str]:
        ret = []
        def aux(offset, exp, value, multed):
            if offset == len(num):
                if value == target:
                    ret.append(exp)
                return
            if max(1, abs(multed)) * (int(num[offset:])) < abs(target - value):
                return
            for i in range(offset, offset + 1 if num[offset]=='0' else len(num)):
                n_str = num[offset:i + 1]
                n_int = int(n_str)
                # this needs for very first call
                if offset == 0:
                    aux(i + 1, n_str, n_int, n_int)
                else:
                    aux(i + 1, exp + '*' + n_str, value - multed + multed * n_int, multed * n_int)
                    aux(i + 1, exp + '+' + n_str, value + n_int, n_int)
                    aux(i + 1, exp + '-' + n_str, value - n_int, -n_int) # note here we put minus
        aux(0, '', 0, 0)
        return ret

if __name__ == "__main__":
    s = SolutionFastest()
    #s.evaluate("4+5*9", True)
    #s.addOperators("00", 0)
    s.addOperators("123", 6)
    s.addOperators("3456237490", 0)
    s.addOperators("105", 5)



