from typing import List


class Solution(object):
    def minDeletionSize(self, A):

        '''
        we greedily check if current column is_sorted if it is we add it to the current string
        '''


        def is_sorted(A):
            return all(A[i] <= A[i+1] for i in range(len(A) - 1))

        ans = 0
        # cur : all rows we have written
        # For example, with A = ["abc","def","ghi"] we might have
        # cur = ["ab", "de", "gh"].
        cur = [""] * len(A)

        for col in zip(*A):
            # cur2 : What we potentially can write, including the
            #        newest column 'col'.
            # Eg. if cur = ["ab","de","gh"] and col = ("c","f","i"),
            # then cur2 = ["abc","def","ghi"].
            cur2 = cur[:]
            for i, letter in enumerate(col):
                cur2[i] = cur2[i] + letter

            if is_sorted(cur2):
                cur = cur2
            else:
                ans += 1

        return ans

class Solution2(object):
    def minDeletionSize(self, A):
        # cuts[i] is True : we don't need to check col[i] <= col[i+1]
        cuts = [False] * (len(A) - 1)

        ans = 0
        for col in zip(*A):
            if all(cuts[i] or col[i] <= col[i+1] for i in range(len(col) - 1)):
                for i in range(len(col) - 1):
                    if col[i] < col[i+1]:
                        cuts[i] = True
            else:
                ans += 1
        return ans

class Solution1:
    def minDeletionSize(self, A: List[str]) -> int:

        def forward():
            cnt = 0
            for j in range(len(A[0])):
                for i in range(len(A) - 1):
                    cur = A[i]
                    nxt = A[i + 1]
                    if cur[j] > nxt[j]:
                        cnt += 1
                        break
                else:
                    return cnt
            return cnt

        def backward():
            cnt = 0
            for j in range(len(A[0]) - 1, -1, -1):
                for i in range(len(A) - 1):
                    cur = A[i]
                    nxt = A[i + 1]
                    if cur[:j + 1] > nxt[:j + 1]:
                        cnt += 1
                        break
                else:
                    return cnt
            return cnt

        print(forward())

        return min(forward(), backward())


if __name__ == '__main__':
    s = Solution2()
    s.minDeletionSize(["xga","xfb","yfa"])