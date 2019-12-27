# https://leetcode.com/problems/find-the-town-judge/
# Treat the input as matrix-adjacency representation
# you will notice that under the judge column there will be all ones except judge itself
# example [[1,3],[2,3]]
#
#  1  2  3
#1 0  0  1
#2 0  0  1
#3 0  0  0
# i.e. the sum of these ones is equal N-1
class Solution:
    def findJudge(self, N: int, trust) -> int:
        # if the trust is empty return 1 (since judge does not trust anybody)
        if len(trust) == 0:
            return 1
        judges = [0]*(N+1)
        current = 0
        index = 0
        for i in range(len(trust)):
            a, b = trust[i]
            judges[a]-=1
            judges[b]+=1
            if judges[b] > current:
                current = judges[b]
                index = b
        return index if judges[index] == N-1 else - 1