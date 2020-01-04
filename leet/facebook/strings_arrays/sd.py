# this technique is called sliding window
# Algo
# create two maps and store count of each letter of strings s1 and s2 with right boundary len(s2)
# Do count the items from two maps with equal letter count
# iterate over s2 starting from 0. Here we will maintain window where left is i and right is i+len(s1)
# Note i+len(s1) will include extra letter because of adding length to index
# in the same loop we are excluding left boundary
# count variable contains number of chars that have equal count in both maps
# that is why we need subtract once when inequality found
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_map = [0] * 26
        s2_map = [0] * 26

        # fill both maps with count of chars in s1 and s2 limited by length of string s1
        for i in range(len(s1)):
            s1_map[ord(s1[i])-97]+=1
            s2_map[ord(s2[i])-97]+=1

        # count is number of chars with equal count in s1_map and s2_map
        count = 0
        # Let's count what we have till now
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                count+=1

        for i in range(len(s2) - len(s1)):
            if count == 26:
                return True
            # this is the window where left pointer is char at s2[i]
            # right pointer is char at s2[i + len(s1)]
            l = ord(s2[i]) - 97
            r = ord(s2[i+len(s1)]) - 97
            s2_map[r]+=1
            if s2_map[r] == s1_map[r]:
                count+=1
            #NOTE: here we decreasing count only if the difference is 1
            #otherwise count would decrease every time and count would be incorrect
            # because count is not a total number of chars
            # count is number of chars with equal count in s1_map and s2_map
            # it is important catch the difference only once
            # let consider s1 = ab s2 = abbbb
            # at the beginnin maps is going to be
            # s1_map = [1,1,0,0,...]
            # s2_map = [1,2,0,0,...] because above we increased it s2_map[r]+=1
            # the next loop we would have [1,3,0,0,...]
            # without this check we would decrease count again which is incorrect
            elif s2_map[r] - s1_map[r] == 1:
                count-=1
            s2_map[l]-=1
            if s1_map[l] == s2_map[l]:
                count+=1
            #NOTE reason is the same as above
            elif s2_map[l] - s1_map[l] == - 1:
                count-=1
        return count == 26

if __name__ == "__main__":
    s= Solution()
    s.checkInclusion("ab", "bbbab")