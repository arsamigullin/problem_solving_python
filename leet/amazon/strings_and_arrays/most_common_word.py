import collections
import typing
List = typing.List
import re
# this problem
# https://leetcode.com/problems/most-common-word/

class SolutionMy:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # r"[a-zA-Z]+" this will filter out only words
        c = collections.Counter(map(str.lower, re.findall(r"[a-zA-Z]+", paragraph)))
        # it is guaranteed that
        for v, count in c.most_common(len(banned) + 1):
            if v not in banned:
                return v
        return ""


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banset = set(banned)
        # first get rid of special chars
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        # count words
        count = collections.Counter(word for word in paragraph.lower().split())

        ans, best = '', 0
        for word in count:
            if count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans