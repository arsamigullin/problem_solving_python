# https://leetcode.com/problems/product-of-array-except-self/

# with division
import math
from typing import List


class MySolution:
    def productExceptSelf(self, nums):
        # pref products technique

        tot = 1  # stores product of all the numbers as it is
        zero_tot = 1  # stores product of all the numbers where but if 0 is met in nums it will replace it with 1
        # to cover cases like [2,3,0], i.e. the product except 0 is 2*3 = 6
        output = [0] * len(nums)
        zero_cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_cnt += 1
            else:
                zero_tot *= nums[i]
            tot *= nums[i]

            # we done here because if nums = [2,3,0,0] the product without first 0 is 0 2*3*0=0
            if zero_cnt > 1:
                return output

        for i in range(len(output)):
            # since in nums we have only one 0 we are using zero_tot
            if nums[i] == 0:
                output[i] = int(zero_tot)
            else:
                output[i] = int(tot / nums[i])
        return output


# without division but having two more arrays  to store the data
class Solution1:
    def productExceptSelf(self, nums):
        left = [1] * len(nums)
        right = [1] * len(nums)

        for i in range(len(nums) - 1):
            left[i + 1] = left[i] * nums[i]
        for i in range(len(nums) - 1, 0, -1):
            right[i - 1] = right[i] * nums[i]
        answer = [0] * len(nums)
        for i in range(len(nums)):
            answer[i] = left[i] * right[i]
        return answer

#without division and with only one array
class Solution2:
    def productExceptSelf(self, nums):
        left = [1] * len(nums)

        for i in range(len(nums) - 1):
            left[i + 1] = left[i] * nums[i]

        answer = [0] * len(nums)
        answer[-1] = left[-1] # no need to calculate the latest item in answer since it is going to be 1 * left[-1]
        r_tmp = 1

        for i in range(len(nums) - 1, 0, -1):
            r_tmp = r_tmp * nums[i]
            answer[i-1] = r_tmp * left[i-1]

        return answer

class Solution4:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nonzeroprod = 1
        zerocnt = 0
        for n in nums:
            if n != 0:
                nonzeroprod*=n
            elif n == 0:
                zerocnt +=1

        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if num == 0 and zerocnt == 1:
                    res[i] = nonzeroprod
            elif zerocnt==0:
                    sign = 1 if (nonzeroprod > 0 and num > 0) or (nonzeroprod<0 and num<0) else -1
                    res[i] = sign * int(round(math.exp(math.log(abs(nonzeroprod)) - math.log(abs(num)))))
        return res


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        nonzeroprod = 1
        zerocnt = 0
        for n in nums:
            if n != 0:
                nonzeroprod *= n
            elif n == 0:
                zerocnt += 1

        for i, n in enumerate(nums):
            if n == 0 and zerocnt == 1:
                res[i] = nonzeroprod
            elif zerocnt == 0:
                nzpd = nonzeroprod
                nzpd = abs(nzpd)
                absn = abs(n)
                for x in range(32)[::-1]:
                    if (nzpd >> x) - absn >= 0:
                        res[i] += 1 << x
                        nzpd -= absn << x
                sign = 1 if (nonzeroprod > 0 and n > 0) or (nonzeroprod < 0 and n < 0) else -1
                res[i] *= sign
        return res

if __name__ == "__main__":
    s = Solution4()
    s.productExceptSelf([1, 2, 3])
