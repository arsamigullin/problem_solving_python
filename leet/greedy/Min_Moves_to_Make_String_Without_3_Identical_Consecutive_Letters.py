# microsoft
# source https://molchevskyi.medium.com/microsoft-interview-tasks-min-moves-to-make-string-without-3-identical-consecutive-letters-abe61ed51a10
# Given a string consisting of only a and b, what is the minimum number of
# swaps(replace a with b or b with a) needed such that string doesn't contain 3 consecutive character which are same. e.g aaaba -> 1 (aabba)

#3 consecutive: baaab, replace the middle a (3 / 3 == 1)
#4 consecutive: baaaab, replace the third a (4 / 3 == 1)
#5 consecutive: baaaaab, replace the third a (5 / 3 == 1)
#6 consecutive: baaaaaab -> baabaaab -> baaab -> bab with 2 replacements (6 / 3 == 2)
#10 consecutive: baaaaaaaaaab -> baabaaaaaaab -> baaaaaaab -> baaaab -> baab with 3 replacements (10 / 3 == 3)

class Solution:
    def replace(self, s):
        replacements = 0
        n = len(s)
        i = 0
        while i < n:
            j = i + 1
            while j < n and s[i] == s[j]:
                j += 1
            replacements += (j - i) // 3
            i = j
        return replacements


if __name__ == '__main__':
    s = Solution()
    print((s.replace("baaaaaaaaaab")))