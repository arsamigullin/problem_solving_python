# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       pass

class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if not self.check(topRight, bottomLeft) or not sea.hasShips(topRight, bottomLeft):
            return 0

        if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
            return sea.hasShips(topRight, bottomLeft)

        midx = (topRight.x - bottomLeft.x) // 2
        midy = (topRight.y - bottomLeft.y) // 2
        midx += bottomLeft.x
        midy += bottomLeft.y
        res = 0

        xt = midx
        yt = midy
        xb = bottomLeft.x
        yb = bottomLeft.y
        res += self.countShips(sea, Point(xt, yt), Point(xb, yb))

        xt = topRight.x
        yt = topRight.y
        xb = midx + 1
        yb = midy + 1
        res += self.countShips(sea, Point(xt, yt), Point(xb, yb))

        xt = midx
        yt = topRight.y
        xb = bottomLeft.x
        yb = midy + 1
        res += self.countShips(sea, Point(xt, yt), Point(xb, yb))

        xt = topRight.x
        yt = midy
        xb = midx + 1
        yb = bottomLeft.y
        res += self.countShips(sea, Point(xt, yt), Point(xb, yb))

        return res

    def check(self, topRight: 'Point', bottomLeft: 'Point'):
        return not (topRight.x < bottomLeft.x or topRight.y < bottomLeft.y)