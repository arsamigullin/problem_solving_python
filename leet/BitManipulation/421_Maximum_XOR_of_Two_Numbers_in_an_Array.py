from typing import List

# the key to solve this problem is to remember
# 1. x^y=z x=z^y y=z^x 7=3^4 3=7^4 4=7^3
# 2.

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        L = len(bin(max(nums)))-2
        max_xor = 0
        for i in range(L-1, -1, -1):
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit, to get rid of 0 is the rightmost bit
            cur_xor = max_xor | 1
            # compute all existing prefixes
            prefixes = {num>>i for num in nums}
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            max_xor |= any(cur_xor^p in prefixes for p in prefixes)
        return  max_xor


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}
        n = len(bin(max(nums))) - 2
        for num in nums:
            node = trie
            for bit in bin(num)[2:].zfill(n):
                bit = int(bit)
                if bit not in node:
                    node[bit] = {}
                node = node[bit]
        max_xor = 0
        for num in nums:
            node = trie
            res = []
            for bit in bin(num)[2:].zfill(n):
                bit = int(bit)
                oppose = bit ^ 1
                if oppose in node:
                    node = node[oppose]
                    res.append(oppose ^ bit)
                else:
                    node = node[bit]
                    res.append(bit ^ bit)
            max_xor = max(max_xor, int(''.join(map(str, res)), 2))

        return max_xor


if __name__ == '__main__':
    s = Solution()
    s.findMaximumXOR([3, 10, 5, 153, 2, 8])
