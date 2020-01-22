class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if len(s) == 0 or len(t) == 0:
            return True
        s_map = [0] * 26
        t_map = [0] * 26
        for i in range(min(len(s), len(t))):
            s_map[ord(s[i]) - 97] += 1
            t_map[ord(t[i]) - 97] += 1
        return s_map == t_map

