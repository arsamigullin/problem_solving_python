 # the most confusing is
 # |n - m| <= 1
 # actually we do not need to specially follow this because this condition will be always met
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        memo = [[-1] * len(s2) for _ in range(len(s1))]

        def helper(i, j, k):
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            if memo[i][j] == -1:
                memo[i][j] = (s1[i] == s3[k] and helper(i + 1, j, k + 1)) or (
                            s2[j] == s3[k] and helper(i, j + 1, k + 1))

            return memo[i][j]

        return helper(0, 0, 0)


class SolutionDP:
 def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

     if len(s1) + len(s2) != len(s3):
         return False

     memo = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
     # memo[0][0] = True
     for i in range(len(s1) + 1):
         for j in range(len(s2) + 1):
             if i == 0 and j == 0:
                 memo[i][j] = True
             elif i == 0:
                 memo[i][j] = memo[i][j - 1] and s2[j - 1] == s3[i + j - 1]
             elif j == 0:
                 memo[i][j] = memo[i - 1][j] and s1[i - 1] == s3[i + j - 1]
             else:
                 memo[i][j] = (memo[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (
                         memo[i - 1][j] and s1[i - 1] == s3[i + j - 1])

     return memo[len(s1)][len(s2)]


 if __name__ == '__main__':
    s = Solution()
    s.isInterleave("aa","ab","abaa")


