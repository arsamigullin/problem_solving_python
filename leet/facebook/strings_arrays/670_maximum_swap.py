# O(n)
class Solution(object):
    '''
    the idea is to replace the smallest number from the left side with greatest value from the right side
    we compose last dict to store value and latest index
    and we also start to traverse from the left side and the current number
    is compared with numbers starting from 9 (since it will bring the greatest result) to the current number

    '''
    def maximumSwap(self, num):
        A = list(map(int, str(num)))
        last = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for d in range(9, x, -1):
                if last.get(d, None) > i:
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num




# Brute force On^3
class SolutionBF:
    def maximumSwap(self, num: int) -> int:

        snum = list(str(num))
        ans = snum[:]
        for i in range(len(snum)):
            for j in range(i + 1, len(snum)):
                snum[i], snum[j] = snum[j], snum[i]
                # do not forget arrays must be copied
                if snum > ans:
                    ans = snum[:]
                # to put the changes back we do the same operation as we did
                # to change it
                snum[i], snum[j] = snum[j], snum[i]
        return int(''.join(ans))

# O(n^2)
class SolutionMy:
    def maximumSwap(self, num: int) -> int:
        snum = list(str(num))
        max_num = max(snum)
        d = {}
        def getDict():
            for i, v in enumerate(snum):
                if v!=max_num:
                    d.setdefault(v, i)
                else:
                    d[v] = i
        getDict()
        max_num = max(d)
        for i, v in enumerate(snum):
            if v!=max_num:
                snum[d[v]], snum[d[max_num]] = snum[d[max_num]], snum[d[v]]
                break
            else:
                seq = snum[i+1:]
                if seq:
                    max_num =  max(seq)
                    d={}
                    getDict()
        return int(''.join(snum))

if __name__ == '__main__':
    s = Solution()
    s.maximumSwap(98368)