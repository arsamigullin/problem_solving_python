class Solution:
    def twoSumLessThanK(self, A: list, K: int) -> int:
        A.sort()
        i, j = 0, len(A) - 1
        last = -1

        def find(start, end, target):
            result = -1
            while start <= end:
                mid = start + (end - start) // 2
                if A[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
                    result = mid
            return result

        def find2(start, end, target):
            result = -1
            while start <= end:
                mid = start + (end - start) // 2
                if A[mid] > target:
                    end = mid - 1
                    result = mid
                else:
                    start = mid + 1
            return result

        index = find2(i, j, K)
        j = index if index > 0 else len(A)
        for i in range(j):
            ind = find(i + 1, j, K - A[i])

            if ind >= 0 and A[ind] + A[i] < K:
                # print(A[ind], A[i])
                last = max(last, A[ind] + A[i])

        return last

# this is well known solution
class Solution:
    def twoSumLessThanK(self, A: list, K: int) -> int:
        A.sort()
        i = 0
        j = len(A) - 1
        max_val = -1
        while i < j:
            total = A[i] + A[j]
            if total < K:
                max_val = max(max_val, total)
                i += 1
            else:
                j -= 1
        return max_val

if __name__ == "__main__":
    s = Solution()
    s.twoSumLessThanK([499,780,837,984,481,526,944,482,862,136,265,605,5,631,974,967,574,293,969,467,573,845,102,224,17,873,648,120,694,996,244,313,404,129,899,583,541,314,525,496,443,857,297,78,575,2,430,137,387,319], 1000)