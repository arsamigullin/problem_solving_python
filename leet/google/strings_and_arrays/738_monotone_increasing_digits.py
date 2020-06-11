# array
# leading zeros removal
#N^2
class SolutionMy:
    def monotoneIncreasingDigits(self, N: int) -> int:
        stack = []
        num = str(N)
        mem = [False] * len(num)
        for i in num:
            stack.append(i)
            for j in range(len(stack) - 1, 0, -1):
                if stack[j - 1] <= stack[j]:
                    break
                stack[j] = '9'
                mem[j] = True
                if not mem[j - 1]:
                    stack[j - 1] = chr(ord(stack[j - 1]) - 1)
        return ''.join(stack).lstrip('0')



#(logN)^2
class Solution1(object):
    def monotoneIncreasingDigits(self, N):
        digits = []
        A = list(map(int, str(N)))
        for i in range(len(A)):
            for d in range(1, 10):
                if digits + [d] * (len(A)-i) > A:
                    digits.append(d-1)
                    break
            else:
                digits.append(9)

        return int("".join(map(str, digits)))


#N
class Solution2(object):
    def monotoneIncreasingDigits(self, N):
        S = list(str(N))
        i = 1
        while i < len(S) and S[i-1] <= S[i]:
            i += 1
        while 0 < i < len(S) and S[i-1] > S[i]:
            S[i-1] = str(int(S[i-1]) - 1)
            i -= 1
        S[i+1:] = '9' * (len(S) - i-1)
        return int("".join(S))

if __name__ == '__main__':
    s = Solution2()
    s.monotoneIncreasingDigits(332)