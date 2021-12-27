class Solution:
    def carFleet(self, target, pos, speed):
        # we sort the cars by their position
        # and then we calculate the time requires to get the target starting from their position
        time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
        print(time)
        res = cur = 0

        time = time[::-1]
        for t in time:
            if t > cur:
                res += 1
                cur = t
        return res



if __name__ == '__main__':
    s = Solution()
    s.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
    s.carFleet(100, [0,2,4], [4,2,1])