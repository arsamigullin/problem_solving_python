import math
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        total_nodes = (1 << len(bin(label)[2:])) - 1
        H = int(math.log(total_nodes + 1, 2) - 1)
        nodes_at_H_level = 2**H
        if H % 2 == 0:
            index = label
        else:
            index = 2*(total_nodes) - nodes_at_H_level + 1 - label
        res = []
        while index>=1:
            total_nodes = 2**(H+1) - 1
            nodes_at_H_level = 2**H
            label = index
            addon = 0 if label % 2 == 0 else 1
            if H%2 == 1:
                label = (2*total_nodes - nodes_at_H_level + 1) - index
                addon = 1 if label % 2 == 0 else 0
            res.append(label)
            index = (index - addon)//2
            H-=1
        return res[::-1]


class Solution1:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        # this is standard formula to get current level
        # since every label is on the same level (labels at odd level reversed, so they just have different position)
        # this formula works
        H = int(math.log(label, 2))
        # the very important thing here is to get the parity at the beginning
        parity = H % 2
        while H != 0:
            H -= 1
            label //= 2
            # This code literally means if the current H does not have the same parity
            # as height of the label node
            # we will do XOR between current label and count of nodes at H level
            if H % 2 != parity:
                ans.append(label ^ (2 ** H - 1))
            else:
                ans.append(label)
        ans.sort()
        return ans


if __name__ == '__main__':
    s = Solution1()
    s.pathInZigZagTree(16)