matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

import heapq

class Solution:
    def kthSmallest(self, matrix: list, k: int) -> int:
        l = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(l, matrix[i][j])
        print(heapq.nsmallest(k, l))[-1]

if __name__ == "__main__":
    s = Solution()
    s.kthSmallest(matrix, 8)
    print('done')