import collections


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        c1 = 0
        c2 = 0
        for i in range(len(s1)):
            # here we just count unmatched chars
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    c1 += 1
                else:
                    c2 += 1
        # it is not possible to make the strings equal if the total unmatched chars odd
        if (c1 + c2) % 2 == 1:
            return -1

        

        return (c1 + 1) // 2 + (c2 + 1) // 2





class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        c1 = collections.Counter(s1)
        c2 = collections.Counter(s2)
        if (c1['x'] + c2['x']) != c1['y'] + c2['y']:
            return -1
        s1 = list(s1)
        s2 = list(s2)


        swaps = 0
        for i in range(len(s1)):
            if s1[i] != s2[i] and s1[i] == 'x':
                for j in range(i + 1, len(s2)):
                    if s2[j] == s2[i]:
                        s1[i], s2[j] = s2[j], s1[i]
                        swaps += 1
                        break
            elif s1[i] != s2[i] and s1[i] == 'y':
                for j in range(i + 1, len(s1)):
                    if s1[j] == s1[i]:
                        s1[j], s2[i] = s2[i], s1[j]
                        swaps += 1
                        break
        return swaps

if __name__ == '__main__':
    s = Solution()
    s.minimumSwap("xxyyxyxyxx", "xyyxyxxxyx")