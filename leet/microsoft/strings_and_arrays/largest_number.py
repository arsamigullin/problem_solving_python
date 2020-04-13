import typing
List = typing.List


class MySolution:
    '''
    The solution is based on Quick sort

    '''
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(n) for n in nums]

        def quick_sort(s, e, A):
            if s < e:
                q = partition(s, e, A)
                quick_sort(s, q - 1, A)
                quick_sort(q + 1, e, A)

        def partition(s, e, A):
            pivot = A[e]
            i = s - 1
            for j in range(s, e):
                # this is only part we changed in our version
                frd = A[j] + pivot
                bkd = pivot + A[j]
                if frd > bkd:
                    i += 1
                    A[i], A[j] = A[j], A[i]

            A[i + 1], A[e] = A[e], A[i + 1]
            return i + 1

        quick_sort(0, len(nums_str) - 1, nums_str)
        return '0' if nums_str[0] == '0' else ''.join(nums_str)


class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


class Solution:
    '''
    This shows how to involve two params when sorting
    '''
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

if __name__ == "__main__":
    s=Solution()
    s.largestNumber([121, 12])
    s.largestNumber([12,121])
    s.largestNumber([135, 75, 35, 350, 350, 3501])
    #s.largestNumber([3,30,34,5,9])