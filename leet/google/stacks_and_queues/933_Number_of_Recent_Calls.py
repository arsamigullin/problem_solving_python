import collections


class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        if not self.q:
            self.q.append(t)
        else:
            while self.q and t - self.q[0] > 3000:
                self.q.popleft()
            self.q.append(t)
        return len(self.q)