import collections
#this problem https://leetcode.com/problems/split-array-into-consecutive-subsequences/

# similar problem
# divide_array_in_sets_of_k_consecutive_numbers.py
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
import itertools
class SolutionGrp(object):
    def isPossible(self, nums):
        prev, prev_count = None, 0
        starts = collections.deque()
        # we do group the nums. Key is num itself and grp is list of the num
        for t, grp in itertools.groupby(nums):
            count = len(list(grp))
            # we must consider only consecutive sequence
            # so if we caught the difference is not 1
            #
            if prev is not None and t - prev != 1:
                # here we determine if we already have have consecutive sequence.
                # Here is example [1,1,1,2,2,2,3,3,3,3,5,6,7]
                # let's suppose we reached 5, i.e. t = 5
                # 5 - 3 !=1 so the consecutiveness is broken
                # now we want to understand if we can start new sequence starting from 5
                # to do that we must make sure that all nums in starts are parts of consecutive sequence
                # at this moment starts = [1,1,1,3] and prev_count is 4 (this count of 3)
                # doing popleft() three times we see that three nums of num 3 are parts of consecutive sequence
                # but when we pop fourth time we see that the fourth 3 is not part of the consecutive sequence, i.e.
                # 3 < 3 + 2
                for _ in range(prev_count):
                    if prev < starts.popleft() + 2:
                        return False
                # and if we have consecutive sequence
                prev, prev_count = None, 0

            if prev is None or t - prev == 1:
                if count > prev_count:
                    for _ in range(count - prev_count):
                        starts.append(t)
                elif count < prev_count:
                    # let's consider this example
                    # [0,1,2,2,2,2,3]
                    # when t is 3, the starts queue is [0,2,2,2]. Those twos were added in the if statement right above
                    # once prev_count > less than count (count of 2(3) is greater count of 3 (1))
                    # we need to make sure all twos are in consecutive sequence
                    # 1 iteration
                    #   t - 1 = 3 - 1 = 2
                    #   starts.popleft() + 2 = 0 + 2
                    #   2<2 is False. This means we found one consecutive sequence
                    # 2 iteration
                    #   t - 1 = 2
                    #   starts.popleft() + 2 = 2 + 2
                    #  2 < 4. This means no consecutive sequences are there anymore. So it is impossible to
                    # split the sequence
                    for _ in range(prev_count - count):
                        if t-1 < starts.popleft() + 2:
                            return False

            prev, prev_count = t, count

        return all(nums[-1] >= x+2 for x in starts)

class Solution(object):
    def isPossible(self, nums):
        count = collections.Counter(nums)
        tails = collections.Counter()
        for x in nums:
            if count[x] == 0:
                continue
            # this check help us to understand if x number can be appended to existing consecutive sequence
            # consider example [1,2,3,4]
            # when x is 4, tails = {4:1}. Tails was gotten from tails[x+3] += 1 below
            # tails says how many consecutive subsequences stopped right before x
            # tails = {4:1} means we have 1 consecutive sequence stopped right before 4, which is {1,2,3}
            # now, if tails[4] > 0, we can append 4 to the {1,2,3}, so we decrease tails[4] and increase tails[5] =1
            # meaning we have 1 consecutive sequence that stopped right before 5
            # NOTE we do this check before checking on consecutive numbers
            elif tails[x] > 0:
                tails[x] -= 1
                tails[x+1] += 1
            elif count[x+1] > 0 and count[x+2] > 0:
                count[x+1] -= 1
                count[x+2] -= 1
                tails[x+3] += 1
            else:
                return False
            count[x] -= 1
        return True


if __name__ == "__main__":
    s = Solution()
    s.isPossible([0, 1,2,2,2,2,3,4, 5, 5, 6, 7, 8])
    s.isPossible([1,2,3,4,5,6])
    s.isPossible([1,1,1,2,2,2,3,3,3,3,4,5,6,7])
    #s.isPossible( [1,1,1,2,2,2,3,3,3,3,5,6,7])

    s.isPossible([0,1,2,5,5,6,7,8])
    #s.isPossible([0,1,2,3,3,4,5])