class Solution:
    def countLetters(self, S: str) -> int:

        cnt = 0
        res = 0
        prev = ""
        for i in range(len(S)):
            if S[i] != prev:
                res += (cnt * (cnt + 1)) // 2
                prev = S[i]
                cnt = 1
            else:
                cnt += 1

        return res + (cnt * (cnt + 1)) // 2
