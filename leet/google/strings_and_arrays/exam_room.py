#https://leetcode.com/problems/exam-room/
class ExamRoom(list):

    def __init__(self, N: int):
        self.N = N

    def seat(self) -> int:
        if not self:
            self.append(0)
            return 0
        else:
            # if student sit at the first place
            dist = 0
            val = 0
            # we do the boundary comparison at the beginning
            # since we need to put the student at lowest seat
            if self[0] != 0:
                dist = self[0]
                val = 0
            # we do finde lowest in the middle
            for i in range(len(self) - 1):
                r = (self[i + 1] - self[i]) // 2
                if r > dist:
                    dist = r
                    val = self[i] + r
            # and only if the end is greater the found distance
            # we do replace it
            if self[-1] != self.N - 1:
                r = self.N - 1 - self[-1]
                if r > dist:
                    dist = r
                    val = self.N - 1

            self.append(val)
            self.sort()
            return val

    def leave(self, p: int) -> None:
        self.remove(p)