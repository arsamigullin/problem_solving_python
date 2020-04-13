import typing
List = typing.List
# this problem
class Solution:
    '''
    1. find count of smallest char in queries
    2. find count of smallest char in words
    3. sort array in point 2
    4. for each count in bullet 1 do binary search of bullet 3
    '''

    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:


        qc = [w.count(min(w)) for w in queries]
        wc = sorted([w.count(min(w)) for w in words])

        # note how binary search is organized
        # this will find latest repeated element
        # for example [3,3,3,4]
        # the result will be pointing to index 2
        def binarysearch(target):
            s = 0
            e = len(wc) - 1 # do not forget subtract 1
            result = e
            while s <= e:
                mid = s + (e - s) // 2
                if target >= wc[mid]:
                    s = mid + 1
                else:
                    result = mid - 1
                    e = mid - 1
            return len(wc) - result - 1

        return list(map(binarysearch, qc))

import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f = sorted(w.count(min(w)) for w in words)
        return [len(f) - bisect.bisect(f, q.count(min(q))) for q in queries]

if __name__ == "__main__":

    # finds the latest repeated target or first minimum
    def binarysearchmin(target, wc):
        s = 0
        e = len(wc) - 1
        result = s
        while s <= e:
            mid = s + (e - s) // 2
            if target >= wc[mid]:
                s = mid + 1
            else:
                result = mid - 1
                e = mid - 1
        return (result, wc[result])

    # finds the latest repeated target or first minimum
    def binarysearchmax(target, wc):
        s = 0
        e = len(wc) - 1
        result = s
        while s <= e:
            mid = s + (e - s) // 2
            if target >= wc[mid]:
                s = mid + 1
                result = mid + 1
            else:
                e = mid - 1
        return (result, wc[result])

    to_find = [3, 4, 5, 3, 1, 1, 1, 2, 1, 6, 3, 3]
    arr = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 7, 7, 7]
    print(binarysearchmax(0, arr))  # returns index 12
    print(binarysearchmin(0, arr)) # returns index 11
    for t in to_find:
        print(binarysearchmin(t, arr))

