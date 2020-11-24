# Algo
# this is dp approach
# initially dp is filled with False except the first elemet
# then we use a well-known approach that checks every index from the beginning till the middle


class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        d = {w:1 for w in wordDict}
        for i in range(1, len(s) + 1):
            for j in range(i):
                print(s[j:i])
                if dp[j] and s[j:i] in d:
                    dp[i] = True
                    break
        return dp[-1]



# Important to sort wordDict because we can inroduce the check
# where once the nextstart is greater that the first word in sorted wordDict we can break
# if the wordDict wouldn't be sorted we would have to traverse the entire array

# another important thing here is d
# if d[i] == True this means since the word wordDict[i] we cannot proceed further, i.e. no way to get other words
# either because the wordDict exhausted or because nextstart is greater that the length of initial string
class SolutionDFS:

    def wordBreak(self, s, wordDict):
        l = len(s)
        d = [False] * l
        di = sorted(wordDict, key = len)

        def _wordBreak(start):
            if d[start]:
                return False

            for w in di:
                nextstart = start + len(w)
                if nextstart > l:
                    break
                if s.startswith(w, start):
                    if nextstart == l or _wordBreak(nextstart):
                        return True
            d[start] = True
            return False

        return _wordBreak(0)

# The same as above but more clean solution
class SolutionDFS1:

    def wordBreak(self, s, wordDict):
        wordDict.sort(key=len)
        # we have dp to keep track on visited start position
        # once the word s reached the length
        dp = [None] * len(s)
        def helper(start):
            if dp[start] is None:
                for w in wordDict:
                    next_start = start + len(w)
                    if s.startswith(w, start):
                        if next_start == len(s) or helper(next_start):
                            dp[start] = True
                            break
                else:
                    dp[start] = False
            return dp[start]
        return helper(0)



if __name__ == "__main__":
    s = SolutionDFS1()
    s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])