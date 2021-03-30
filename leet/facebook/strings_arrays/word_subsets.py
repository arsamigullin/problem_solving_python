# this problem
# https://leetcode.com/problems/word-subsets/
import collections
import typing
List = typing.List
class Solution:
    '''
    it says each word in B must be subset of word in A
    No need to compare each word of B with each word of A

    It is only enough to count max count of occurences of each letter in B

    for example B = [aab, bba]
    we want to count max occurence of a in b. Since 'a' occurs twice in the first word and 'b' occurs twice in the
    the second word the max occurences are db = {'a':2, 'b':2}
    '''

    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        db = {}
        for b in B:
            d = {}
            for c in b:
                d[c] = d.get(c,0) + 1
            for k in d:
                db[k] = max(db.get(k, 0), d[k])
        res = []
        for a in A:
            d = {}
            for c in a:
                d[c] = d.get(c,0) + 1
            if all([k in d and db[k]<=d[k] for k in db]):
                res.append(a)
        return res


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dictsA = [collections.Counter(a) for a in A]
        dictB = collections.defaultdict(int)

        for b in B:
            bc = collections.Counter(b)
            for key in bc:
                dictB[key] = max(dictB[key], bc[key])
        res = []
        for i, da in enumerate(dictsA):
            isUniversal = True
            for kb in dictB.keys():
                if not (kb in da and dictB[kb] <= da[kb]):
                    isUniversal = False
                    break
            if isUniversal:
                res.append(A[i])
        return res

if __name__ == "__main__":
    s = Solution()
    s.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["lo","eo"])