import typing
List = typing.List
class Solution:
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

if __name__ == "__main__":
    s = SolutionLoop()
    #s.evaluate("4+5*9", True)
    #s.addOperators("00", 0)
    s.addOperators("3456237490",9191)


