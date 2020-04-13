# this problem
# https://leetcode.com/problems/vowel-spellchecker/
import typing
List = typing.List

# When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
# When the query matches a word up to capitlization, you should return the first such match in the wordlist.
# When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
# If the query has no matches in the wordlist, you should return the empty string.

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        perfect = set(wordlist) # perfect words are in priority
        capwords = {}
        vowwords = {}
        def devowel(wrd):
            return ''.join(['*' if w in 'aeiou' else w for w in wrd])


        for word in wordlist:

            wordlow = word.lower()
            # caps diffs in second priority
            capwords.setdefault(wordlow, word)
            # vowel diffs in third priority
            vowwords.setdefault(devowel(wordlow), word)

        def helper(wrd):

            if wrd in perfect:
                return wrd
            wordlow = wrd.lower()
            if wordlow in capwords:
                return capwords[wordlow]
            devowrd = devowel(wordlow)
            if devowrd in vowwords:
                return vowwords[devowrd]
            return ""

        return map(helper, queries)

if __name__ == "__main__":

    s = Solution()
    s.spellchecker(["KiTe","kite","hare","Hare"],
["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"])