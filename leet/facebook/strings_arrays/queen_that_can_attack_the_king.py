import typing
List = typing.List
# avg = 60ms
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        chessboard = [[0]*8 for _ in range(8)]
        result = []
        for x,y in queens:
            chessboard[x][y] = 1
        #print(chessboard)
        directions = [(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(0,-1),(1,0),(-1,0)]
        for rowOffset, colOffset in directions:
            s, e = king[0] + rowOffset, king[1] + colOffset
            while 0<=s<8 and 0<=e<8:
                if chessboard[s][e] == 1:
                    result.append([s,e])
                    break
                s+=rowOffset
                e+=colOffset
        return result

# avg = 40ms
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result = []
        directions = [(1,1),(-1,-1),(-1,1),(1,-1),(0,1),(0,-1),(1,0),(-1,0)]
        for rowOffset, colOffset in directions:
            s, e = king[0] + rowOffset, king[1] + colOffset
            while 0<=s<8 and 0<=e<8:
                if [s,e] in queens:
                    result.append([s,e])
                    break
                s+=rowOffset
                e+=colOffset
        return result