import collections

class Solution:
    '''
    let's consider example AAABB and k = 1
    '''
    def characterReplacement(self, s, k):
        counts = collections.defaultdict(int)
        ret = i = n = 0
        for j, c in enumerate(s):
            counts[c] += 1
            # here we take only the letters with most counts in rang till j
            if counts[c] > n:
                n = counts[c]
            # j - i is total count of letters between j and i
            # j - i - n is count of letters that is not equal the letter with count n
            # so, if for example j = 4 (B), the count of A (3) is greater the count of B(2)
            # there is no sense to subtract count of B since it will provide shortest sequence when replacing A letters
            # since n is count of A, by j - i - n we see, how many letters are not A
            # and if this count is greater than allowed number(K) we decrease sliding window
            if j - i - n >= k:
                counts[s[i]] -= 1
                i += 1
            # at this moment we can calculate the result
            if j - i >= ret:
                ret = j - i + 1
        return ret
if __name__ == "__main__":
    s = Solution()
    s.characterReplacement("ABAB",2)