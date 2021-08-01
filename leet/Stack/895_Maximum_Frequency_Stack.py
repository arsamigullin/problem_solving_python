import collections


class FreqStack(object):

    def __init__(self):
        # num - count dict. Used to update maxfreq
        self.count = collections.Counter()
        # freg - nums dict. Used to group items by freq. For example, [1,2,2,3].
        # group[1] = [1,2,3]
        # group[2] = [2]
        # maxfreq = 2
        self.group = collections.defaultdict(list)
        self.max_count = 0

    def push(self, x):
        f = self.count[x] + 1
        self.count[x] = f
        if f > self.max_count:
            self.max_count = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.max_count].pop()
        self.count[x] -= 1
        # once the elements under the frequency exhausted
        # decrease the freq
        # Since group does gropping the numbers by count
        # and if we pushed three nums, say [5,5,5], 5 is going to be in all groups 1,2,3, i.e.
        # group[1] = [5]
        # group[2] = [5]
        # group[3] = [5]
        if not self.group[self.max_count]:
            self.max_count -= 1

        return x

if __name__ == '__main__':
    s = FreqStack()
    s.push(5)
    s.push(7)
    s.push(5)
    s.push(7)
    s.push(4)
    s.push(5)
    s.pop()
    s.pop()
    s.pop()
    s.pop()