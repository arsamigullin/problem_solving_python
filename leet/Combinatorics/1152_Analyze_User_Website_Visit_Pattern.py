import collections
import itertools
from _ast import List
import  bisect

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        user_visits = collections.defaultdict(list)
        for i, user in enumerate(username):
            user_visits[user].append((timestamp[i], website[i]))
        three_seq = collections.defaultdict(dict)
        max_count = 0
        for i, user in enumerate(user_visits.keys()):
            if len(user_visits[user]) < 3:
                continue
            sorted_by_time = [w for _, w in sorted(user_visits[user], key=lambda x: x[0])]
            for (a, b, c) in itertools.combinations(sorted_by_time, 3):
                three_seq[(a, b, c)][user] = 1
                max_count = max(max_count, len(three_seq[(a, b, c)]))

        comm = sorted([k for k, v in three_seq.items() if len(v) == max_count])

        return comm[0]


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        user_visits = collections.defaultdict(list)
        for user, time, web in zip(username, timestamp, website):
            user_visits[user].append((time, web))

        combs = collections.defaultdict(set)

        max_count = 0
        for user in user_visits:

            web = [w for time, w in sorted(user_visits[user])]
            if len(web) < 3:
                continue
            user_combs = itertools.combinations(web, 3)
            for first, sec, third in user_combs:
                combs[(first, sec, third)].add(user)
                max_count = max(max_count, len(combs[(first, sec, third)]))
        arr = sorted([visits for visits, users in combs.items() if len(users) == max_count])

        return arr[0]

