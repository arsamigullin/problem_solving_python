# 1461. Check If a String Contains All Binary Codes of Size K
# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/solution/
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # this is the same as 2**k
        need = 1 << k
        got = [False]*need
        # (2**n) -1 in binary representation gives us all ones
        # for example, n = 5, 2**5-1=31, bin(31) = 0b11111
        all_one = need - 1
        hash_val = 0

        for i in range(len(s)):
            # calculate hash for s[i-k+1:i+1]
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            # hash only available when i-k+1 > 0
            if i >= k-1 and got[hash_val] is False:
                got[hash_val] = True
                need -= 1
                if need == 0:
                    return True
        return False

if __name__ == '__main__':
    s = Solution()
    s.hasAllCodes("00110110", 2)