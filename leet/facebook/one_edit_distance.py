#161 https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        if abs(ns - nt) > 1:
            return False

        i, j = 0, 0
        diff_count = 0
        oper_type = 1  # replace
        if len(s) > len(t):
            oper_type = 2  # remove
        elif len(s) < len(t):
            oper_type = 3  # add

        while i < ns and j < nt:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                diff_count += 1
                if diff_count > 1:
                    return False
                # since it is we just increasing two pointers
                if oper_type == 1:
                    i += 1
                    j += 1
                # since it is removal we just increasing pointer of s
                elif oper_type == 2:
                    i += 1
                # since it is addition we just increasing pointer of j
                else:
                    j += 1

        # if s/t shorter than t/s there could be a situations where latest item is not covered since
        # i/j reached length of s/t
        # for example s=ab t=abs
        if diff_count == 0:
            diff_count = abs(ns - nt)

        return True if diff_count == 1 else False


class TheirSolution:
    def isOneEditDistance(self, s: 'str', t: 'str') -> 'bool':
        ns, nt = len(s), len(t)

        # Ensure that s is shorter than t.
        if ns > nt:
            return self.isOneEditDistance(t, s)

        # The strings are NOT one edit away distance
        # if the length diff is more than 1.
        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # if strings have the same length
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                # if strings have different lengths
                else:
                    return s[i:] == t[i + 1:]

        # If there is no diffs on ns distance
        # the strings are one edit away only if
        # t has one more character.
        return ns + 1 == nt

if __name__ == "__main__":
    s = Solution()
    s.isOneEditDistance("abcdf","ab4d")
    ts = TheirSolution()
    ts.isOneEditDistance("cab" ,"ad")