import typing
List = typing.List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        MAX = 4294967296
        def helper1(i, tot, prev, fibs):
            if i >= len(S):
                return len(fibs) >=3
            limit = len(S)-1 if tot < 0 else len(str(tot))
            step = 1 if tot < 0 else len(str(tot))
            while step <= limit + 1:
                cur_str = S[i: i + step]
                cur = int(cur_str)
                if (len(cur_str) > 1 and cur_str[0] == '0') or cur > MAX or cur + prev > MAX:
                    return False
                if cur == tot or tot == -1:
                    nex_tot = cur + prev
                    fibs.append(cur)
                    if helper1(step + i, nex_tot, cur, fibs):
                        return True
                    fibs.pop()
                step += 1
            return  False

        data = []
        for j in range(0, len(S)-3):
            step = 1
            while j + step < len(S)-2:
                str_f = S[j:j + step]
                f = int(str_f)
                if (len(str_f)>1 and str_f[0] == '0') or f > MAX:
                    return []
                data.append(f)
                if helper1(j + step, -1, f, data):
                    return data
                data.pop()
                step+=1

        return data


class SolutionIterative(object):
    def splitIntoFibonacci(self, S):
        for i in range(min(10, len(S))):
            x = S[:i+1]
            if x != '0' and x.startswith('0'): break
            a = int(x)
            for j in range(i+1, min(i+10, len(S))):
                y = S[i+1: j+1]
                if y != '0' and y.startswith('0'): break
                b = int(y)
                fib = [a, b]
                k = j + 1
                while k < len(S):
                    nxt = fib[-1] + fib[-2]
                    nxtS = str(nxt)
                    if nxt <= 2**31 - 1 and S[k:].startswith(nxtS):
                        k += len(nxtS)
                        fib.append(nxt)
                    else:
                        break
                else:
                    if len(fib) >= 3:
                        return fib
        return []

if __name__ == "__main__":
    s = Solution()
    # s.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")
    # s.splitIntoFibonacci("10588")
    # s.splitIntoFibonacci("1101111")
    # #s.splitIntoFibonacci("0123")
    # #s.splitIntoFibonacci("112358130")
    s.splitIntoFibonacci("11235813")
    # #s.splitIntoFibonacci("123456579")