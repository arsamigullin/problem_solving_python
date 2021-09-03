import typing
List = typing.List

# these two most popular
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        options = [set()]
        # O(n * m * 2 ^ n)
        arr = [set(word) for word in arr if len(word) == len(set(word))]
        result = 0
        # print(arr)
        for word in arr:
            for option in options:
                composed_word = option | word
                if len(composed_word) == len(word) + len(option):
                    options.append(composed_word)
                    result = max(result, len(composed_word))

        return result
# O(nm)+O(n*2^n)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        nums = []
        # O(n*m) where n is len(arr) and m is max len of the word in arr
        for a in arr:
            if len(a) == len(set(a)):
                num = 0

                for ch in a:
                    num|=1<<ord(ch)-ord('a')
                nums.append(num)
        n = len(arr)


        def helper(i, cur):
            if i>=len(nums):
                return bin(cur).count('1')
            if cur|nums[i] == cur+nums[i]:
                return max(helper(i+1,cur+nums[i]), helper(i+1, cur))
            else:
                return helper(i+1, cur)
        res= 0
        # O(n*2^n)
        for i in range(len(nums)):
            res = max(res, helper(i, nums[i]))
        return res

#############
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        if not arr:
            return []
        bitarray = []
        for i in range(len(arr)):

            if len(set(arr[i])) != len(arr[i]):
                continue
            num = 0
            for j in range(len(arr[i])):
                num |= 2 ** (ord(arr[i][j]) - ord('a'))
            bitarray.append(num)
        d = {}
        def helper(i, cur_max):

            if i == len(bitarray):
                return bin(cur_max).count('1')
            key = f"{bitarray[i]}|{cur_max}"
            if key in d:
                return d[key]
            if bitarray[i]&cur_max == 0:
                m = max(helper(i+1,bitarray[i]|cur_max), helper(i+1, cur_max))
            else:
                m = max(helper(i+1, bitarray[i]),helper(i+1, cur_max))
            d[key] = m
            return m
        return helper(0, 0)


from collections import Counter


class SolutionShortFast:
    def maxLength(self, arr: List[str]) -> int:
        arr = [s for s in arr if len(s) == len(set(s))]
        if not arr:
            return 0

        arr.sort(key=len, reverse=True)
        print(arr)
        max_len = 0

        for i in range(len(arr)):
            tmp = arr[i]
            for j in range(len(arr)):
                if not set(tmp) & set(arr[j]):
                    tmp += arr[j]
            max_len = max(max_len, len(tmp))

        return max_len

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        r = [set()]
        for s in arr:
            if (len(set(s)) < len(s)):
                continue
            s = set(s)
            for c in r:
                if s & c:
                    continue
                r.append(s|c)
        return max(len(a) for a in r)


if __name__ == "__main__":
    s=SolutionShortFast()
    s.maxLength(["a", "abc", "d", "de", "def"])
    s.maxLength(["enrgbdwhqpo","bioedlpz","nfampjeycstxbz","almhiqdypr","qaxldwmgk","mpfgislz","g","yjlipemkuxqsctforbw","udylqhogvfmwikat","euzrimspyfanvlkhb","ltekhadr","wvagsjrzlobm"])
    s.maxLength(["ab","cd","cde","cdef","efg","fgh","abxyz"])