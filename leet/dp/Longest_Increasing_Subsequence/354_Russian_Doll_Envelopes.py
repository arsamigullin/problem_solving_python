from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        # the key trick here is to sort the list also by -x[1]
        # x[0] - width, x[1] - height
        # Say we have this example [[1, 3], [1, 4], [2, 3], [1, 5]]
        # sorting only by width gives the height in the following order 3,4,5,3
        # LIS algo will find 3,4,5 as the longest subsequence
        # and it seems like we 3 fits 4, 4 fits 5 but we cannot do that because their width are the same (1)
        # sorting also by -x[1] gives us 5,4,3,3. The LIS here is only one which is the correct answer
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        dp = [0] * n
        end = 0
        # this is standard LIS with O(nlgn) complexity
        for _, e in envelopes:
            # regular binary search (bisect_left)
            lo = 0
            hi = end
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if e > dp[mid]:
                    lo = mid + 1
                else:
                    hi = mid

            dp[lo] = e
            if lo == end:
                end += 1

        return end

if __name__ == '__main__':

    s = Solution()
    s.maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]])
    s.maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1], [1, 1]])
    s.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]])
