from typing import List


class Solution:
    '''
    We use binary search here based on this statement:
    "if there is a duplicate substring of length k, that means that there is a duplicate substring of length k - 1.
    Hence one could use a binary search by string length here, and have the first problem
    solved in \mathcal{O}(\log N)O(logN) time."

    in other words, if we found that the substring of len k has duplicate in the string then we do not need to find
    the substring of less len and we will try to find substring of greater len by increasing lo (lo = mid).
    mid represents the length of substring we search duplicates for
    we return lo since lo always will be pointing to the mid


    '''
    def longestRepeatingSubstring(self, S: str) -> int:
        def possible(k):
            seen = set()
            for i in range(len(S) - k + 1):
                sub = S[i:i + k]
                if sub in seen:
                    return True
                else:
                    seen.add(sub)
            return False

        lo, hi = 0, len(S) - 1
        while lo < hi:
            mid = hi - (hi - lo)//2
            if not possible(mid):
                hi = mid - 1
            else:
                lo = mid
        return lo


class Solution:
    '''
    Rolling hash : hash generation in a constant time
    '''
    def search(self, L: int, a: int, modulus: int, n: int, nums: List[int]) -> str:
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # compute the hash of string S[:L]
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus

        # already seen hashes of strings of length L
        seen = {h}
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2 ** 24

        # binary search, L = repeating string length
        left, right = 0, n - 1
        while left <= right:
            L = right - (right - left) // 2 # (mid)
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L - 1

        return left - 1

if __name__ == '__main__':
    s = Solution()
    s.longestRepeatingSubstring("aabcaabdaab")
    s.longestRepeatingSubstring("aaaaa")
