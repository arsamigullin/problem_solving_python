class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def find(i, j, st, pat, cnt):
            if i == len(st):
                if cnt >= len(st) and j>=len(p)-1:
                    return True
                else:
                    return False
            if j == len(p):
                return False
            #elif i == len(st) or j == len(pat):
            #   return False

            if st[i] == pat[j]:
                return find(i + 1, j + 1, st, pat, cnt + 1)
            elif pat[j] == '*':
                if j - 1 < 0:
                    return False
                elif st[i] == pat[j - 1] or pat[j-1] == '.':
                    return find(i + 1, j, st, pat, cnt + 1)
                else:
                    return find(i, j + 1, st, pat, cnt + 1)
            elif pat[j] == '.':
                return find(i + 1, j + 1, st, pat, cnt + 1)
            elif j+1<len(pat) and pat[j + 1] == "*":
                return find(i, j+2, st, pat, cnt)
            else:
                return False
        return find(0,0,s,p,0)

if __name__ == "__main__":
    s = Solution()
    s.isMatch("aaa", "aaaa")
    s.isMatch("aaa", "aaaa")
    s.isMatch("ab", ".*c")
    s.isMatch("aab", "c*a*b")
    #s.isMatch("mississippi", "mis*is*p*.")