import collections
from typing import List

class Solution:
    def numSquarefulPerms(self, A):
        c = collections.Counter(A)
        cand = {i: {j for j in c if int((i + j) ** 0.5) ** 2 == i + j} for i in c}

        def dfs(x, left=len(A) - 1):
            c[x] -= 1
            count = sum(dfs(y, left - 1) for y in cand[x] if c[y]) if left else 1
            c[x] += 1
            return count

        return sum(map(dfs, c))

# the same as above but more readable
# Q: why cannot we just use the same solution as in Permutation 2
# A: because it traverses all members of the c dictionary. In the current problem we need to traverse
# over the candidate children, so it is necessary to pass the candidate as a parameter
# Q: why there could not be duplicates
# A: because candidates is a dict and we traverse over the dict
class Solution7:
    def numSquarefulPerms(self, A):
        # this is for backtracking and see we even can use the number
        c = collections.Counter(A)
        d = collections.defaultdict(set)
        # compose graph where children are nums that gives perfect square with the key
        # for example 8:{1,17,8}, 8+1 =9, 8+17=25, 8+8=16
        for i in c:
            for j in c:
                if int((j + i) ** 0.5) ** 2 == j + i:
                    d[i].add(j)

        # left is steps left
        def dfs(node, left=len(A) - 1):
            if left == 0:
                return 1
            # node is now taken
            c[node] -= 1
            count = 0
            # this is like graph traversing
            for ch in d[node]:
                if c[ch] > 0:
                    count += dfs(ch, left - 1)
            c[node] += 1
            return count

        return sum(map(dfs, c))


class Solution1:
    def numSquarefulPerms(self, nums: List[int]):
        nums.sort()
        n = len(nums)
        count = 0
        visited = set()

        def helper(i):
            nonlocal count
            if i >= n:
                count += 1
                return

            for j in range(i, n):
                if j > i and nums[i] == nums[j]:
                    continue
                if (i, nums[j]) not in visited:
                    visited.add((i, nums[j]))
                    nums[j], nums[i] = nums[i], nums[j]
                    if i == 0 or (int((nums[i] + nums[i - 1]) ** 0.5) ** 2 == nums[i] + nums[i - 1]):
                        helper(i + 1)
                    #nums[j], nums[i] = nums[i], nums[j]

        helper(0)
        return count

class Solution:
    def numSquarefulPerms(self, nums: List[int]):
        nums.sort()
        n = len(nums)
        count = 0
        visited = set()

        def helper(i):
            nonlocal count
            if i >= n:
                count += 1
                return

            for j in range(i, n):
                if j > i and nums[i] == nums[j]:
                    continue
                if (i, nums[j]) not in visited:
                    visited.add((i, nums[j]))
                    nums[j], nums[i] = nums[i], nums[j]
                    if j == 0 or (j > 0 and int((nums[j] + nums[j - 1]) ** 0.5) ** 2 == nums[j] + nums[j - 1]):
                        helper(j + 1)
                    nums[j], nums[i] = nums[i], nums[j]

        helper(0)
        return count


if __name__ == '__main__':
    s =Solution7()
    s.numSquarefulPerms([1, 1, 8, 1, 8])
    s.numSquarefulPerms([1, 17, 8])
    s.numSquarefulPerms([2,3,1])

