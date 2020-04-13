from typing import List
# this problem
# https://leetcode.com/problems/find-and-replace-in-string/

class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        offset = 0
        res = S
        # it is important to sort indexes, sources and targets by indexes
        # because that way we need to take care of only the right part of string
        # let's suppose we have unsorted indexes [6,2,1]
        # after replacing word from index 6 in original string we will have offset = len(target) - len(source)
        # then we replacing string from index 2 and we are going to apply offset
        # but at index 2 no offset should be applied yet

        for i, source, target in sorted(zip(indexes, sources, targets)):
            if S[i: i + len(source)] == source:
                # here we cut off original string and put target string
                res = res[:i + offset] + target + res[i + offset + len(source):]
                offset += len(target) - len(source)
        return res

