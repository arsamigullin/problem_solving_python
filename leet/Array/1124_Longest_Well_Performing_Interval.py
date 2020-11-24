from typing import List


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        '''
        example [9,9,6,0,6,6,9]
        1 iter
        i = 0
        S = 1
        ans = 1
        d = {1: 0}

        2 iter
        i = 1
        S = 2
        ans = 2
        d = {1:0, 2:1}

        3 iter
        i = 2
        S = 2
        ans =
        '''
        d = {}
        S = 0
        ans = 0
        for i in range(len(hours)):
            S += (1 if hours[i] > 8 else -1)
            if S > 0:
                ans = i + 1
            if S - 1 in d:
                ans = max(ans, i - d[S - 1])
            d.setdefault(S, i)
        return ans



class Solution1:
    def longestWPI(self, hours: List[int]) -> int:
        H = {0: -1}
        Max, Sum = 0, 0
        for i in range(len(hours)):
            Sum += hours[i]
            if Sum > 0:
                Max = i + 1
            else:
                if Sum - 1 in H:
                    Max = max(Max, i - H[Sum - 1])
            if not Sum in H: H[Sum] = i
        return Max

if __name__ == '__main__':
    s = Solution()
    s.longestWPI([9,9,6,0,6,6,9])