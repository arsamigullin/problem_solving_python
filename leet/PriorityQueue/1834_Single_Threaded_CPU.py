import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        Constraints:
        - CPU processes task with shortest process time
        - No delay between start and finish
        - enqueTime, is when the task was available to process
        Approach
        - Sorting + heap
          - We can sort arry by enqueTime, process time
          - For each iteration; add task to the heap, and process task with lowest process time if the enquie time is right
          - Time, space: o(n log(n)), o(n)
        '''
        tasks = sorted([t + [i] for i, t in enumerate(tasks)])
        heap, ans = [], []
        last_end = 0
		#Process Tasks
        for start, duration, idx in tasks:
            while heap and last_end < start:
                dur, i, e = heapq.heappop(heap)
                last_end = max(e, last_end) + dur
                ans.append(i)
            heapq.heappush(heap, (duration, idx, start))
        #Empty heap
        while heap:
            _, i, _ = heapq.heappop(heap)
            ans.append(i)
        return ans

if __name__ == '__main__':
    s = Solution()
    s.getOrder([[1,2],[2,4],[3,2],[4,1]])