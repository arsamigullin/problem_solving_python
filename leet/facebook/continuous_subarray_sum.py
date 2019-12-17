import collections
class Solution:
    # we are storing reminders in hashtable(let's denote it d)
    # let's consider an example
    # nums: [2, 5, 33, 6, 7, 25, 15] and k=13
    # when i = 1 the sum is gonna be 2 + 5 = 7 and we will store in d the reminder 7%13 = 7
    # then we continue to sum items, so 7 + 33 = 40 and we store reminder 40%13=1 in d
    # after adding 6, i.e. 40+6 we get 46 and reminder is 46%13=7
    # but we already have reminder 7 in d. This means the sum of latest two numbers (33 + 6) is divisible by k
    # because reminder the same!!!!
    # So, if we encountered reminder second time it means the sum of elements since that reminder divisible by k
    # in our case
    # 7%13=7 46%13=7 46(2+5+33+6) - 7(2+5) = 39
    # 39%13 == 0

    def checkSubarraySum(self, nums, k):
        d = collections.defaultdict(int)
        d[0] = -1
        _sum = 0
        for i in range(len(nums)):
            _sum+=nums[i]
            rem = _sum
            if k != 0:
                rem = _sum % k
            if rem in d:
                if i - d[rem] > 1:
                    return True
            else:
                d[rem] = i
        return False

if  __name__ == "__main__":
    s = Solution()
    s.checkSubarraySum([0,0], 0)