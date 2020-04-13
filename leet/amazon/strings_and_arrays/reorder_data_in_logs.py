from typing import List


class SolutionMy:
    '''
    Here I am shifting digit logs to the left
    since it will keep their order

    and then we have j which is pointing to the index where letter log starts
    We do custom sorting
    '''
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        i, j = 0, 0
        while i < len(logs):
            if logs[i][logs[i].find(' ') + 1].isdigit():
                logs[j], logs[i] = logs[i], logs[j]
                j += 1
            i+=1
        def sortkey(x):
            i = x.find(' ') + 1
            return x[i:], x[:i]
        logs[j:] = sorted(logs[j:], key=sortkey)
        return logs[j:] + logs[:j]


class Solution(object):
    def reorderLogFiles(self, logs):
        def f(log):
            id_, rest = log.split(" ", 1)
            return (0, rest, id_) if rest[0].isalpha() else (1,)

        return sorted(logs, key = f)
