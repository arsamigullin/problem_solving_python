# My Solution
# It is working fast as well
# Observation
# We think this problem in terms of intervals
# Once we found not intersecting interval, this is the needed cut point

# Algo
# 1. Keep intervals of each letter [start, end]
# 2. sort by start time
# 3. take the first interval as the correct one
# 4. Once we've met not intersecting interval, cut partition (add the index to the result)
class MySolution:
    def partitionLabels(self, S: str) -> list:
        d = {}
        #1
        for i, s in enumerate(S):
            if s in d:
                d[s][1] = i
            else:
                d[s] = [i, i]
        #2
        intervals = sorted(d.values(), key=lambda k: k[0])
        res = []
        dif = 0
        #3
        gr_start, gr_end = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            #4
            if gr_end < start:
                res.append(gr_end + 1 - dif)
                dif = gr_end + 1
                gr_end = end
            else:
                gr_end = max(end, gr_end)
        res.append(gr_end + 1 - dif)
        return res


# Short greedy solution
# store the very last positions
# Iterating over each letter in string we find the current max
# All the letters less that current maximum will be ignored since max(j, last[i])
# once current index is equal current maximum, partition the string (add to ans)
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1

        return ans

if __name__ == "__main__":
    s =Solution()
    s.partitionLabels("ababcbacadefegdehijhklij")