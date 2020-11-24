import collections
import heapq
import math

# similar 1054. Distant Barcodes

import collections
import heapq
# correct solution
class Solution:
    '''
    NOTE: 'x' < 'z'. if we have to compare two tuples (-2, 'x') and (-2,'z'), then (-2, 'x') is less than (-2,'z')
    '''

    def rearrangeString(self, s, k):
        if k < 2: return s

        hp, q, ans = [], collections.deque(), []
        for c, count in collections.Counter(s).items():
            heapq.heappush(hp, (-count, c))

        # this check can be ommited
        # since we have this one
        # ''.join(ans) if len(ans) == len(s) else '' at the end
        if (k * (-hp[0][0] - 1)) + 1 > len(s):
            '''
            consider k = 3 and 'xxxxyyyzzab', len is 11
            (3 * (4-1)) + 1 = 10 (4 is count of x)
            '''
            return ''  # not possible if too many of max freq. char

        while hp:
            # this will always the char with max count since we did count * (-1) and this is heap
            count, c = heapq.heappop(hp)
            # we can freely add the char to the answer
            ans.append(c)
            # since we added char on previous command we must decrease count of the char
            q.append((count + 1, c) if (count < -1) else None)
            # this condition allows us to keep the same char apart k chars
            # that is, we do pop from queue only if its size greater or equal than k
            # before that we are collecting in answer different chars
            # since we popped them out from heap
            if len(q) >= k:
                cand = q.popleft()
                if cand:
                    # since this heap the chars with max count will be first
                    heapq.heappush(hp, cand)

        return ''.join(ans) if len(ans) == len(s) else ''

if __name__ == "__main__":
    s = Solution()
    s.rearrangeString("zzxxyy",2)
    #s.rearrangeString("xxxxyyyzz", 2)

class Solution2:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1 or k > len(s):
            return s
        c = collections.Counter(s)
        m = c.most_common(1)[0][1]
        if k * (m - 1) >= len(s):
            return ""

        cs = c.most_common()
        # print(cs)
        res = [None] * len(s)
        q = collections.deque()
        heap = [num for num in range(k)]
        heapq.heapify(heap)
        # print(heap)
        i = 0
        while heap:
            # print(res, heap)
            start = heapq.heappop(heap)

            ch, cnt = cs[i]
            l = start + k * (cnt - 1)
            res[start:l + 1:k] = [ch] * cnt
            if l + k < len(s):
                heapq.heappush(heap, l + k)
            i += 1

        return ''.join(res)




class Solution1:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1 or k > len(s):
            return s
        c = collections.Counter(s)
        cs = c.most_common()
        groups = []
        r = len(s)
        i = 0

        def find(m):
            for j in range(m, k-1, -1):
                d, rem = divmod(r, j)
                if rem in (0, j-1):
                    p = r
                    while p not in (0,-1):
                        start = groups[-1][1] if groups else 0
                        end = start + j
                        groups.append((start, end))
                        p -= j
                    return True
            return False

        while r >= 0:
            if cs[i][1] > k:
                shift = cs[i][1]
                if groups:
                    start = groups[-1][1]
                    end = start + shift
                else:
                    start = 0
                    end = shift
                groups.append((start, end))
                r -= shift
                if r < shift - 1:
                    return ""
                elif shift - 1 <= r <= shift:
                    break
            else:
                max_shift = max(cs[0][1], k)
                if find(max_shift):
                    break
                else:
                    return ""
            i+=1
        #k = max(k, math.ceil(len(s)/cs[0][1]))
        res = [None] * len(s)
        j = 0
        for i,(start, e) in enumerate(groups):
            res[j::k] = s[start:e]
            j+=1

        print(groups)




class AttemptSolution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1 or k > len(s):
            return s
        c = collections.Counter(s)

        return ""

        cs = c.most_common()
        K = k + 1 if len(cs) > k and k % 2 == 0 else k
        # print(cs)
        res = [None] * len(s)
        q = collections.deque()
        heap = [num for num in range(K)]
        heapq.heapify(heap)
        # print(heap)
        i = 0
        while heap:
            print(res, heap)
            start = heapq.heappop(heap)
            ch, cnt = cs[i]
            l = start + K * (cnt - 1)
            res[start:l + 1:K] = [ch] * cnt
            if l + K < len(s):
                heapq.heappush(heap, l + k)
            i += 1

        return ''.join(res)


import collections
import heapq
import math


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1 or k > len(s):
            return s
        c = collections.Counter(s)
        cs = c.most_common()

        b = max(cs[0][1], k)
        print(b)
        grp_cnt = math.ceil(len(s) / b)
        if grp_cnt < k:
            return ""

        res = [None] * len(s)
        i = 0
        items = list(c.elements())
        for j in range(b):
            for g in range(grp_cnt):
                c = j + g * b
                print(c)
                if c < len(s):
                    # print(res)
                    res[i] = items[c][0]
                    i += 1
        return ''.join(res)

