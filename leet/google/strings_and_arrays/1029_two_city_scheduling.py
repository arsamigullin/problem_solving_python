from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        #costs = [[i,a,b] for i,(a,b) in enumerate(costs)]
        A = sorted([(i,a) for i, (a, _) in enumerate(costs)], key=lambda x: x[1], reverse=True)
        B = sorted([(i,b) for i, (_, b) in enumerate(costs)], key=lambda x: x[1])
        visited=set()
        i, j = 0, len(costs) - 1
        isBcity = True
        tot = 0
        while i<=j:
            curindex = j
            curList = A
            if isBcity:
                curindex = i
                curList = B
            k, val = curList[curindex]
            if k in visited:
                if isBcity:
                    i+=1
                else:
                    j-=1
                continue
            visited.add(k)
            tot+=val
            if isBcity:
                i+=1
            else:
                j-=1
            isBcity^=1
        return tot
if __name__ == '__main__':
    s = Solution()
    s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]])