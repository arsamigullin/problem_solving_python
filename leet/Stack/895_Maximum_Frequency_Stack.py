import collections


class FreqStack(object):

    def __init__(self):
        # num - count dict. Used to update maxfreq
        self.freq = collections.Counter()
        # freg - nums dict. Used to group items by freq. For example, [1,2,2,3].
        # group[1] = [1,2,3]
        # group[2] = [2]
        # maxfreq = 2
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        # once the elements under the frequency exhausted
        # decrease the freq
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x