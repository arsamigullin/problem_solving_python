# say we have shelf
# books count 2 4 5 6 7
# index       0 1 2 3 4
# at books[4] we have 7 books
# at books[3] we expect to have books[3] >= books[4] - 1
# at books[2] we expect to have books[2] >= books[4] - 2 and so on
# in general case at book[j] we expect to have
# books[j]>=books[i]−(i−j), for example books[1]>=books[4]-(4-1) => 4>=7-(4-1) => 4>=4 or in more generic way
# books[j]>=books[i] - (cnt - 1) where cnt is number of summands, meaning
# books[4] = books[i] - (cnt(1)-1) = books[4] - 0 = 7
# books[3] = books[i] - (cnt(2)-1) = books[4] - 1 = 6
# books[2] = books[i] - (cnt(3)-1) = books[4] - 2 = 5 and so on
# this in turn can be rewritten
# books[j]-j>=books[i]−i
# one more thing, the books[1:5] subbarray forms arithmetic progression and sum of that subarray can be calculated in O(1)
# the formula is 0.5*(lastItem - firstItem)*cnt
# the sum of books[1:5] is 0.5*(7+4) * 4 = 0.5*11*4=22
# OR since the firstItem is books[i] and lastItem is books[i] - (cnt-1) we have
# 0.5 * (books[i] + books[i] - (cnt-1)) * cnt = 0.5 * (2 * books[i] - (cnt-1)) * cnt

from typing import List


class Solution:
    def maximumBooks(self, books: List[int]) -> int:

        n = len(books)
        dp = [0] * n
        stack = []

        def get_count(l, r):
            # taking min is important here for the cases when books[r] == 0
            # also for this test case [0,3,1,5,4]
            cnt = min(books[r], r-l+1)
            return 0.5 * (2*books[i] - (cnt-1)) * cnt

        for i in range(n):

            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            if not stack:
                dp[i] = get_count(0, i)
            else:
                j = stack[-1]
                dp[i] = dp[j] + get_count(j+1, i)

            stack.append(i)
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    s.maximumBooks([0,3,1,5,4])
    s.maximumBooks([7,0,3,4,5])
    s.maximumBooks([7,8,9,10])
    s.maximumBooks([1,2,3,4])
    s.maximumBooks([8,5,2,7,9])