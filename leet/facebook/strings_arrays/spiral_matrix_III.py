# Algo
# There is a pattern when moving spirally 1,1,2,2,3,3,4,4,5,5,
# this means 1 step we move to the est, 1 to the south, 2 to the west and 2 to the north, 3 to the east , 3 to the south...
# we can observe west and north are different from east and south by 1
# the max limit for k (distance to walk to either direction) is a perimeter(why it is so, still not clear)
import typing
List = typing.List
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = [[r0, c0]]
        if R*C ==1:
            return ans
        for k in range(1,2*(C+R),2):
            for rowOffset, colOffset, dist_to_walk in ((0,1,k),(1,0,k),(0,-1,k+1),(-1,0,k+1)):
                for _ in range(dist_to_walk):
                    r0+=rowOffset
                    c0+=colOffset
                    if 0<=r0<R and 0<=c0<C:
                        ans.append([r0,c0])
                        if len(ans) == C*R:
                            return ans
if __name__ == "__main__":
    s =  Solution()
    s.spiralMatrixIII(5,6,1,4)