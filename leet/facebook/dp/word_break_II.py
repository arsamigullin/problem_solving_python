class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:

        d = [True] * (len(s) + 1)
        print(wordDict)
        l = len(s)
        res = []

        def helper(wrd, i):
            if not d[i]:
                return False
            lr = False
            for word in wordDict:
                nextstart = i + len(word)
                if nextstart > l:
                    continue
                if s.startswith(word, i):
                    if nextstart == l:
                        res.append(wrd + ('' if not wrd else ' ') + word)
                        return True
                    else:
                        #if d[i]:
                            #return False
                        lr|=helper(wrd + ('' if not wrd else ' ') + word, nextstart)
            d[i] = lr
            return d[i]
        helper('', 0)

        return res

# Memory Limit Exceeded

class Solution:
    def wordBreak(self, s: str, wordDict: list) -> list:

        d = [[] for _ in range(len(s)+1)]
        print(d)
        d[0] = ['']
        for i in range(1, len(s) + 1):
            lst = []
            for j in range(i):
                if len(d[j]) > 0 and s[j:i] in wordDict:
                    for wd in d[j]:
                        lst.append(wd + ('' if not wd else ' ') + s[j:i])
            d[i] = lst
        return d[-1]


if __name__ == "__main__":
    s = Solution()
    #s.wordBreak("pineapplepenapple",["apple", "pen", "applepen", "pine", "pineapple"])
    s.wordBreak("catsanddog",["cat","cats","and","sand","dog"])