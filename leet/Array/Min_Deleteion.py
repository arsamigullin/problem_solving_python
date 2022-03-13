import collections


class Solution:
    def solve(self, arr, cost):

        c = collections.Counter(arr)
        tot_cost = 0
        for ch, count in c.items():
            tot_cost += cost[ord(ch)-ord('a')] * (count-1)
        return tot_cost

if __name__ == '__main__':
    s = Solution()
    print(s.solve('aabbbc',[1,2,3]))