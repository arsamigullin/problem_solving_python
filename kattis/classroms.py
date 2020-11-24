import sys
from heapq import heappop, heappush, heappushpop
from collections import  deque
from bisect import bisect_left
def main1():
    # lines = sys.stdin.readlines()
    # count = 0
    # n, k = map(int, lines[0].split())
    # intervals = [(int(s), int(e)) for s, e in range(1, len(lines))]
    n=8
    k=2
    intervals = [(2,4),(6,8),(10,15),(1,3),(5,11),(3,5),(7,10),(12,14)]
    count = 0
    q = deque()
    #intervals.sort(key=lambda x: (x[0], x[1] - x[0]))
    intervals.sort(key=lambda x: x[1])
    for s, e in intervals:
        if len(q) < k:
            q.append(e)
            count+=1
        else:
            i = bisect_left(q, s-1)
            if i == len(q):
                q[-1] = e
                count += 1
            elif q[i] < s:
                q[i] = e
                count+=1
            elif i-1>=0 and q[i-1]<s:
                q[i-1] = e
                count+=1
        # if k > 0:
        #     heappush(heap, e)
        #     k -= 1
        #     count += 1
        # else:
        #     fe = heap[0]
        #     if s > fe:
        #         heappushpop(heap, e)
        #         count += 1
    return count

if __name__ == '__main__':
    main1()

# import sys
# from heapq import heappop, heappush, heappushpop
#
# import sys
# from heapq import heappop, heappush, heappushpop
#
#
# def main():
#     lines = sys.stdin.readlines()
#     count = 0
#     n, k = map(int, lines[0].split())
#     intervals = [(int(lines[i][0]), int(lines[i][1])) for i in range(1, len(lines))]
#     heap = []
#     for s, e in intervals:
#         if k > 0:
#             heappush(heap, (e, s))
#             k -= 1
#             count += 1
#         else:
#             fe, fs = heap[0]
#             if s > fe:
#                 heappushpop(heap, (e, s))
#                 count += 1
#     return count


#main()

