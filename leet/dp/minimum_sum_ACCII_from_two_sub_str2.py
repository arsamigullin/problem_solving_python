
# this solution is not working but has some interesting technique
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        lookup = self.LCSLength(s1, s2)
        n = len(s1)
        m = len(s2)
        l = self.LCS(s1, s2, n, m, lookup)
        tot_s1 = sum([ord(ch) for ch in s1])
        tot_s2 = sum([ord(ch) for ch in s2])
        min_sum = max(tot_s1, tot_s2)
        for word in l:
            comm_total = sum([ord(ch) for ch in word])
            min_sum = min(min_sum, tot_s1 + tot_s2 - 2 * comm_total)
        return min_sum

    def LCSLength(self, s1, s2):
        l = [[0 for i in range(1001)] for j in range(1001)]
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                if s1[i - 1] == s2[j - 1]:
                    l[i][j] = l[i - 1][j - 1] + 1
                else:
                    l[i][j] = max(l[i - 1][j], l[i][j - 1])
        return l

    def LCS(self, s1, s2, n, m, lookup):
        if n == 0 or m == 0:
            return [""]
        if s1[n - 1] == s2[m - 1]:
            seq_list = self.LCS(s1, s2, n - 1, m - 1, lookup)

            for i in range(len(seq_list)):
                seq_list[i] = seq_list[i] + s1[n - 1]
            return seq_list

        if lookup[n][m - 1] > lookup[n - 1][m]:
            return self.LCS(s1, s2, n, m - 1, lookup)

        if lookup[n - 1][m] > lookup[n][m - 1]:
            return self.LCS(s1, s2, n - 1, m, lookup)

        top = self.LCS(s1, s2, n - 1, m, lookup)
        left = self.LCS(s1, s2, n, m - 1, lookup)
        top += left
        return top