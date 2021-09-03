import string
'''
The idea is to count substrings where a particular char is unique
for examples, XAXXAXBAZ
let's count how many substrings exists where char A is unique
We can put ) somewhere between first and the second A and then somewhere between 
the second A and third A. The total substrings count is (i-j)*(j-k) where i,j,k are indices of first second and third A 
'''

class Solution:
    def uniqueLetterString(self, s: str) -> int:
        index = {letter: [-1, -1] for letter in string.ascii_uppercase}
        res = 0
        n = len(s)

        # the first loop is always results in 0 because
        # (X-(-1))*(-1-(-1)) = Y*0=0 where X is any index
        for i, ch in enumerate(s):
            p, q = index[ch]
            res += (i - q) * (q - p)
            index[ch] = [q, i]

        for ch in index:
            p, q = index[ch]
            res += (n - q) * (q - p)
        return res

if __name__ == '__main__':
    s = Solution()
    s.uniqueLetterString("XAXAXXAX")