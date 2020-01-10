class Solution:
    def findAnagrams(self, s: str, p: str):
        if len(p) > len(s):
            return []
        s_map = [0] * 26
        p_map = [0] * 26
        # since p is alway less or equal s
        for i in range(len(p)):
            s_map[s[i] - 97] += 1
            p_map[p[i] - 97] += 1
        count = 0
        # count the chars which have the same count
        # Note: if both are
        for i in range(26):
            if p_map[i] == s_map[i]:
                count+=1

        for i in range(len(s) - len(p)):


