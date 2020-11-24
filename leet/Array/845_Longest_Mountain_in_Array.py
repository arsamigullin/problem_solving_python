from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        UPHILL, DOWNHILL, SURF, NONE = 0, 1, 2, 4
        cnt = 0
        c = 0
        state = prevstate = SURF
        start = False
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                state = UPHILL
                start = True
            elif A[i - 1] > A[i]:
                state = DOWNHILL
            elif A[i - 1] == A[i]:
                state = SURF
            if state == UPHILL and (prevstate == DOWNHILL or prevstate == SURF):
                cnt = max(cnt, c)
                c = 1
            elif (state == UPHILL) or (state == DOWNHILL and (prevstate == DOWNHILL or prevstate == UPHILL)):
                c += 1
            elif state == SURF and prevstate == DOWNHILL:
                start = False
                cnt = max(cnt, c)
                c = 0
            prevstate = state
        if state == DOWNHILL and start:
            cnt = max(cnt, c)
        return cnt + 1 if cnt > 0 else 0

if __name__ == '__main__':
    s = Solution()
    s.longestMountain([2,0,2,2,3])

