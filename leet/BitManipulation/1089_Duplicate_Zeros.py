import collections
from typing import List

# O(n) O(1)
class SolutionO1:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0


# O(n) O(n)
class SolutionOn:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        queue = collections.deque()
        n = len(arr)
        for i in range(n):
            if arr[i]==0:
                queue.append(arr[i])
            if queue:
                num = queue.popleft()
                queue.append(arr[i])
                arr[i] = num

class SolutionMy:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zerocnt = arr.count(0)
        temp = [0] * (len(arr) + zerocnt)
        zer = 0
        for i, val in enumerate(arr):
            if val == 0:
                zer += 1
            else:
                temp[i + zer] = val
            arr[i] = temp[i]


class Solution1:
    def duplicateZeros(self, arr: List[int]) -> None:

        for i, x in enumerate(arr[::-1]):
            if x == 0:
                arr.insert(~i, 0)
                arr.pop(-1)


class Solution2:
    def duplicateZeros(self, arr: List[int]) -> None:
        len_ = len(arr)
        i = 0
        while (i < len_):
            if arr[i] == 0:
                arr.insert(i, 0)
                arr.pop()
                i += 2
                continue
            else:
                i += 1

# interesting approach on Java
# int n = arr.length, z = 0;
#         for (int x: arr)
#             z = x==0? z+1: z;
#         for (int j = n-1;j>=0 && z>0;j--) {
#             if (arr[j]>0) {
#                 if (j+z<n)
#                     arr[j+z] = arr[j];
#             }
#             else {
#                 if (j+z<n)
#                     arr[j+z] = arr[j];
#                 if (j+z-1<n)
#                     arr[j+z-1] = arr[j];
#                  --z;
#             }
#         }


if __name__ == '__main__':
    s = SolutionO1()
    s.duplicateZeros([1,0,2,3,0,4,5,0])