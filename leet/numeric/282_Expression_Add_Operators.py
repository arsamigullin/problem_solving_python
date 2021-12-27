from typing import List


class Solution2:
    def addOperators(self, num: str, target: int):

        n = len(num)
        result = []

        def helper(i, last_num, calc_result, expression):
            if i >= n:
                if calc_result == target:
                    result.append(expression)
                return

            for j in range(i, n):
                num_now_str = str(num[i:j + 1])
                print(num_now_str)
                if len(num_now_str) > 1 and num_now_str[0] == '0':
                    break
                num_now = int(num[i:j + 1])

                if i == 0:
                    helper(j + 1, num_now, num_now, num_now_str)
                else:
                    helper(j + 1, num_now, calc_result + num_now, expression + '+' + num_now_str)
                    helper(j + 1, -num_now, calc_result - num_now, expression + '-' + num_now_str)
                    # this is the trickiest part
                    # we keep track of last_num to use it when mul
                    # for example, num_last=2, result 10. NOTE: num_last already sitting in result
                    # that is why when doing result + num_last*num_now we also must subtract num_last
                    # to cancel it out
                    helper(j + 1, last_num * num_now, calc_result - last_num + last_num * num_now,
                           expression + '*' + num_now_str)

        helper(0, 0, 0, '')
        return result

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        ans = []
        def dfs(start, num_last, result, tmp):
            if start == n:
                if result == target:
                    ans.append(tmp)
                return
            for i in range(start+1, n+1):
                if i > start+1 and num[start] == '0':
                    break
                num_now_str = num[start:i]
                num_now = int(num[start:i])
                if start == 0:
                    dfs(i, num_now, num_now, num_now_str)
                else:
                    dfs(i, num_now, result+num_now, tmp+'+'+num_now_str)
                    dfs(i, -num_now, result-num_now, tmp+'-'+num_now_str)
                    # this is the trickiest part
                    # we keep track of last_num to use it when mul
                    # for example, num_last=2, result 10. NOTE: num_last already sitting in result
                    # that is why when doing result + num_last*num_now we also must subtract num_last
                    # to cancel it out
                    dfs(i, num_last*num_now, result-num_last+num_last*num_now, tmp+'*'+num_now_str)
        dfs(0, 0, 0, '')
        return ans


class Solution:
    def addOperators(self, num: str, target: int):

        ops = []
        nums = []
        result = set()
        n = len(num)

        def helper(i, op, nums, expression):
            if i >= n:
                if len(nums) == 1 and nums[0] == target:
                    result.add(''.join(expression[:-1]))
                    return
                temp_nums = nums[::]
                #print(temp_nums, op)
                for i in range(len(op)-1)[::-1]:
                    last = temp_nums.pop()
                    first = temp_nums.pop()
                    if op[i] == '*':
                        temp_nums.append(first * last)
                    elif op[i] == '-':
                        temp_nums.append(first - last)
                    else:
                        temp_nums.append(first + last)
                if temp_nums[0] == target:
                    result.add(''.join(expression[:-1]))
                return
            for k in range(i, n):
                is_mul = False
                cur = int(num[i:k+1])
                if op and op[-1] == '*':
                    op.pop()
                    is_mul = True
                    nums[-1] = nums[-1] * cur
                else:
                    nums.append(cur)

                expression.append(num[i:k+1])
                for operand in ['*', '-', '+']:
                    expression.append(operand)
                    op.append(operand)
                    helper(k+1, op, nums, expression)
                    op.pop()
                    expression.pop()
                expression.pop()
                if is_mul:
                    op.append('*')
                    if cur!=0:
                        nums[-1] = nums[-1] // cur
                else:
                    nums.pop()
                if num[i:k+1] == '0':
                    return

        helper(0, [], [], [])
        return result

if __name__ == '__main__':
    s = Solution2()
    s.addOperators("105", 5)
    s.addOperators("00", 0)


    s.addOperators("123", 6)