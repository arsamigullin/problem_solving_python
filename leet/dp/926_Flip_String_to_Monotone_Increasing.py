
class Solution(object):
    def minFlipsMonoIncr(self, s):
        n = len(s)
        num_0 = s.count('0') # we assume that we flipped all zeros
        res = num_0
        left_1, right_0 = 0, num_0

        for i in range(n):
            # now we try to cancel flip of 0 we did above with s.count('0')
            if s[i] == '0':
                right_0-=1
            # here we try to flip 1 since we only flipped 0 and did not flip 1 yet
            elif s[i] == '1':
                left_1+=1
            # and here we are finding result
            res = min(res, right_0 + left_1)
        return res


if __name__ == '__main__':
    s = Solution()
    s.minFlipsMonoIncr("00110")