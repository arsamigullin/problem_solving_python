from typing import List


# this problem
# https://leetcode.com/problems/add-bold-tag-in-string/

# Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b>
# and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap,
# you need to wrap them together by only one pair of closed bold tag.
# Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

class Solution:
    '''
    let's understand what is overlapping substring
    let's consider example
    s = "bcaaabbcc"
    dict = ["bcaa","aab","bc"]
    the first word bcaa is in s starting from index 0 and ends at index 3
    the second word aab is in s starts from index 3 and ends at index  5
    so, these two words are overlapping in s and we must treat them as single word

    below algorithm handles this
    '''

    def addBoldTag(self, s: str, dict: List[str]) -> str:
        status = [False] * len(s)
        final = []
        for word in dict:
            l = len(word)
            i = s.find(word)
            while i != -1:
                status[i:i + l] = [True] * l
                i = s.find(word, i + 1)
        i = 0
        while i < len(s):
            # we put consecutive letters with an appropriate consecutive True status
            if status[i]:
                final.append("<b>")
                while i < len(s) and status[i]:
                    final.append(s[i])
                    i += 1
                final.append("</b>")
            else:
                final.append(s[i])
                i += 1
        return "".join(final)


if __name__ == "__main__":
    s = Solution()
    s.addBoldTag("aaabbcc", ["aaa", "aab", "bc"])
