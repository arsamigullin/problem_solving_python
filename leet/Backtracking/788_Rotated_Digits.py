# the option without memo
class Solution:
    def rotatedDigits(self, n: int) -> int:

        numLen = len(str(n))
        goodDict = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '9': '6', '8': '8'}

        def countGoodNumbers(curNum):
            if len(curNum) >= numLen:
                cur = int(''.join(curNum))
                rot = int(''.join([goodDict[m] for m in curNum]))
                return n >= rot != cur
            cnt = 0
            for num in ['1', '2', '5', '6', '9', '8', '0']:
                curNum.append(num)
                cnt += countGoodNumbers(curNum)
                curNum.pop()
            return cnt

        return countGoodNumbers([])

# turned out memo is not required
class Solution:
    def rotatedDigits(self, n: int) -> int:

        numLen = len(str(n))
        goodDict = {'0': '0', '1': '1', '2': '5', '5': '2', '6': '9', '9': '6', '8': '8'}
        memo = {}
        rep = 0

        def countGoodNumbers(curNum):
            nonlocal rep
            if len(curNum) >= numLen:
                cur = int(''.join(curNum))
                rot = int(''.join([goodDict[m] for m in curNum]))
                return n >= rot != cur
            t = tuple(curNum)
            if t not in memo:
                cnt = 0
                for num in ['1', '2', '5', '6', '9', '8', '0']:
                    curNum.append(num)
                    cnt += countGoodNumbers(curNum)
                    curNum.pop()
                memo[t] = cnt
            else:
                rep += 1
            return memo[t]

        res = countGoodNumbers([])
        print(rep) # reps is always 0
        return res


class Solution:
    def rotatedDigits(self, N: int) -> int:
        d = {'5': '2', '2': '5', '9': '6', '6': '9', '1': '1', '0': '0', '8': '8'}
        nums = list(map(str, range(0, N + 1)))
        print(nums)

        def getRotatedNum(num):
            res = ''
            for n in num:
                val = d.get(n, '*')

                if val == '*':
                    return 0
                res += val

            return res != num

        return sum(getRotatedNum(num) for num in nums)