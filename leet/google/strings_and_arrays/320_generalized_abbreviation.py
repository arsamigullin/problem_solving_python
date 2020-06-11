from typing import List


# bit manipulation solution
# does not work nes
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        ans = []
        x = 0
        while True:
            if x >= 1 << len(word):
                break
            x += 1
            ans.append(self.abbr(word, x))

        return ans

    def abbr(self, word, x):
        k = 0
        n = len(word)
        arr = []
        for i in range(n):
            if x & 1 == 0:
                if k != 0:
                    arr.append(str(k))
                    k = 0
                arr.append(word[i])
            else:
                k += 1
            x >>= 1
        if k != 0:
            arr.append(str(k))
        return ''.join(arr)


if __name__ == '__main__':
    s = Solution()
    s.generateAbbreviations("word")

# How many abbreviations are there for a word of length nn? The answer is 2^(N)
#   because each character can either be abbreviated or not, resulting in different abbreviations.

class MySolution:
    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        res = [word]

        def helper(start, w):
            if start >= len(w):
                return
            while start < len(w):
                for i in range(1, n + 1):
                    if start + i > len(w):
                        break
                    num = str(i)
                    wrd = w[:start] + num + w[start + i:]
                    res.append(wrd)
                    helper(start + len(num) + 1, wrd)
                start += 1

        helper(0, word)
        return res


class Solution:
    def generateAbbreviations(self, word):
        dp = {}
        dp[''] = ['']
        return self.gar(word, dp)

    def gar(self, word, dp):
        if word not in dp:
            allres = [word]
            for p in range(len(word)):
                for l in range(1, len(word) + 1 - p):
                    res = self.gar(word[p + l + 1:], dp)
                    pre = word[:p] + str(l) + word[p + l:p + l + 1]
                    res = [pre + x for x in res]
                    allres.extend(res)
            dp[word] = allres
        return dp[word]


class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:

        def backtrack(word, index, cur, count):
            if len(word) == index:
                # Once we reach the end, append current to the result
                res.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                backtrack(word, index + 1, cur, count + 1)
                # Include current position, and zero-out count
                backtrack(word, index + 1, cur + (str(count) if count > 0 else '') + word[index], 0)

        res = []
        backtrack(word, 0, '', 0)
        return res
