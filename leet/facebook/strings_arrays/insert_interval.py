# this problem
# https://leetcode.com/problems/insert-interval/

# similar problem
#https://leetcode.com/problems/merge-intervals/

# The best solution

class Solution:
    '''
    Consider example [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    after adding new iterval we sort it by start item
    [[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]
    The further explanation is simple:
    if end of previous interval is greater start of new interval then this is new interval (add it to res)
    else update end value of previous added with max value of previous added interval and current interval
    1 iteration 
        res is empty we add it to res
        res = [[1,2]]
    2 iteration
        2 not greater 3, hence [3,5] is new interval, we add it to res
        res= [[1,2],[3,5]]
    3 iteration 
        3 > 4, we have overlap, update end value with max(5,8)
        res= [[1,2],[3,8]]
    4 iteration 
        8 > 6, we have overlat, update end value with max(8,7)
        res= [[1,2],[3,8]]
    5 iteration 
        8 == 8, we have overlap, update end value with max(8,8)
        res= [[1,2],[3,10]]
    6 iteration
        10<12, no overlap. Add it to the res
        res =  [[1,2],[3,10],[12,16]]
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda k: k[0])
        res = []
        for i in range(len(intervals)):
            s, e = intervals[i]
            if not res or res[-1][1] < s:
                # this is a new interval
                res.append([s,e])
            else:
                # update end of interval
                res[-1][1] = max(res[-1][1], e)
        return res

# My Optimized version
class Solution:
    '''
    Algo:
    1. Add the new interval to the interval list
    2. Split interval list to two halves: starts (will contain only start position) and ends(will contain only end positions)
    3. Sort starts and ends lists
    4. fix k (this is start of merged intervals)
    5. Let's consinder example [[]]

    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        starts = sorted([item[0] for item in intervals])
        ends = sorted([item[1] for item in intervals])
        
        i, j, k = 0, 0, -1
        res = []
        while i < len(starts):
            k = i if k==-1 else k
            if starts[i] <= ends[j]:
                if i == len(starts)-1:
                    res.append([starts[k], ends[i]])
                i+=1
            else:
                if starts[i] > ends[i-1]:
                    res.append([starts[k], ends[i-1]])
                    k=-1
                j = i

        return res
# this solution inspired by 
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda k: k[0])
        current = [intervals[0][0], intervals[0][1]]
        res = [current]
        for i in range(1, len(intervals)):
            s1, e1 = current
            s2, e2 = intervals[i]
            if e1>=s2:
                current[1] = max(e1,e2)
            else:
                current = [s2, e2]
                res.append(current)
        return res
        

class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        starts = sorted([item[0] for item in intervals])
        ends = sorted([item[1] for item in intervals])
        
        i,j=0,0
        res = []
        while i < len(starts):
            k = i
            while k < len(starts):
                if starts[k] <= ends[j]:
                    if k == len(starts)-1:
                        res.append([starts[i], ends[k]])
                        i = k + 1
                        break
                    else:
                        k+=1
                else:
                    if starts[k] > ends[k-1]:
                        res.append([starts[i], ends[k-1]])
                        i = j = k
                        break
                    else:
                        j = k

        return res


        