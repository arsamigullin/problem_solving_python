class SolutionWrong:
    def isMatch(self, s: str, p: str) -> bool:

        def find(i, j, st, pat, cnt):
            if i == len(st):
                if cnt >= len(st) and j>=len(p)-1:
                    return True
                else:
                    return False
            if j == len(p):
                return False
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




class Solution(object):
    '''
    Without asterix the code would look so
    def match(text, pattern):
        if not pattern: return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        return first_match and match(text[1:], pattern[1:])
    '''

    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        # check if the first char matches (. means Matches any single character)
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        # if the second item in pattern is Asterix (which means Matches zero or more of the preceding element)
        # we try to ignore that part of pattern, so * represents 0 of the preceding element OR
        # only if the firsh_match is True, we can remove the matched character in the text
        # that way we emulate * representing 1 of the preceding element
        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])


if __name__ == "__main__":
    s = Solution()
    s.isMatch("aaaab", "a*b")
    s.isMatch("aa", "a*")
    s.isMatch("aaa", "aaaa")
    s.isMatch("aaa", "aaaa")
    s.isMatch("ab", ".*c")
    s.isMatch("aab", "c*a*b")
    #s.isMatch("mississippi", "mis*is*p*.")