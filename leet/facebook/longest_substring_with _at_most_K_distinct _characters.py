# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
# window technique

#Now one could write down the algortihm.

#Return 0 if the string is empty or k is equal to zero.
#Set both set pointers in the beginning of the string left = 0 and right = 0 and init max substring length max_len = 1.
#While right pointer is less than N:
#Add the current character s[right] in the hashmap and move right pointer to the right.
#If hashmap contains k + 1 distinct characters, remove the leftmost character from the hashmap and move the left pointer so that sliding window contains again k distinct characters only.
#Update max_len.
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # IMPORTANT! we store the latest index of a char NOT count
        d = dict()
        max_len = 0
        i = 0
        j = 0
        while i < len(s):
            # refresh/store the latest index of s[i] char
            d[s[i]] = i
            i+=1
            # once we exceeded the k
            if len(d) > k:
                del_idx = min(d.values())
                d.pop(s[del_idx], None) # remove a key with a smallest index
                j = del_idx + 1 # increase left boundary
            total = max(total, i + 1 - j)
            i += 1
        return max_len
