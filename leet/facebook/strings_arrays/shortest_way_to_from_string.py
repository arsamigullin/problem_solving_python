# Algo
# once the chars in both source ant target are equal
# increase both pointers
# if i pointer never changed after the second loop
# this means the char was not found in source, return -1
class MySolution:
    def shortestWay(self, source: str, target: str) -> int:
        if target == source:
            return 1
        cnt = 0
        i, j = 0, 0
        while i < len(target):
            prev = i
            j = 0
            while j < len(source) and i < len(target):
                if source[j] == target[i]:
                    j += 1
                    i += 1
                else:
                    j += 1
            if prev == i:
                return -1
            cnt += 1

        return cnt

# the fatest solution
# next array technique
# For each char in source we store array[26] that stores indexes
# for example, the source 'abc' with 0,1,2 indexes accordingly
# we create arr(len(source)) and starting form the end of source we populate arr
# with array[26] where we put index to the char location
#[
#    [0, 1, 2...],
#    [-1, 1, 2...],
#    [-1, -1, 2...]
#]
class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        if not target:
            return 0
        if len(set(target) - set(source)):
            return -1
        if target == source:
            return 1

        base = ord('a')
        sourceNextArr = self.buildNextArr(source, base)

        i, j, count = 0, 0, 0
        while j < len(target):
            # NOTE: we start from i = 0
            # and we pulling out index of an approprite char of target in next array
            # if we found the char we jump to the next to this char position (iNex+1) position
            # Once we exceeded i we return -1
            iNext = sourceNextArr[i][ord(target[j]) - base] if i < len(source) else -1
            if iNext == -1:
                count += 1
                i = 0
            else:
                i = iNext + 1
                j += 1
        return count + 1

    # here we create 2d array where row count is len(s) and col count is 26
    # this array represents the presence(actually index) of char in source
    def buildNextArr(self, s, base):
        last = [-1] * 26
        result = [None] * len(s)
        for i in range(len(s) - 1, -1, -1):
            last[ord(s[i]) - base] = i
            result[i] = last[:]
        return result

if __name__ == "__main__":
    s = Solution()
    s.shortestWay("abcde", "bb")
    s.shortestWay("aaa","aaaaa")
    s.shortestWay("abc","abcbc")