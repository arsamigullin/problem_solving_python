import typing
List = typing.List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        mustbe = list(range(0, len(arr) + 1)) # this works faster than sorting arr
        cnt = 0
        i = 0
        step = 1
        # mustbe array is already sorted
        # we take chunk from arr and check to see if this sorted chunk is equal to mustbe chunk
        while i < len(arr) and step <= len(arr):
            if sorted(arr[i:i + step]) == mustbe[i:i + step]:
                cnt += 1
                if step >= len(arr):
                    break
                i = i + step
                step = 1
            else:
                step += 1
        return cnt


class Solution(object):
    '''
    let's suppose we have array arr = [1,0,4,3,2]
    1 iteration i = 0
        ma = max(0,1) = 1
        i = 0, i!=ma 0!=1
    2 iteration i = 1
        ma = max(1,0) = 1
        i==ma 1!=1 ans+=1

    3 iteration i = 2
        ma = max(1,4) = 4
        i!=ma 2!=4

    4 iteration i = 3
        ma = max(3,4) = 4
        i!=ma 3!=4

    5 iteration i = 4
        ma = max(2,4) = 4
        i==ma 4==4 ans+=1
    '''
    def maxChunksToSorted(self, arr):
        ans = ma = 0
        for i, x in enumerate(arr):
            ma = max(ma, x)
            if ma == i:
                ans += 1
        return ans


class Solution(object):
    def maxChunksToSorted(self, arr):
        s1 = 0
        s2 = 0
        ans=0
        for X, Y in zip(arr, sorted(arr)):
            s1+=X
            s2+=Y
            if s1==s2:
                ans+=1
        return ans

