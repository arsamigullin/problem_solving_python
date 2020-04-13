import typing
List = typing.List
class Solution:
    '''
    Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
    Return the number of nice sub-arrays.

    We do count even numbers
    evens array consist count of evens split by odds
    Consider an example
    2221221222
    evens array will be [3,2,3]
    since we neccesarily must have exactly k numbers of odds
    evens[0]+1 count of combination before the first 1
    evens[0+k]+1 count of combination after the last array
    to get res we multiply them to get

    According to Levin
    "The multiplicative principle states that if event A can occur in m ways,
    and each possibility for A allows for exactly n ways for event B , then
    the event “ A and B ” can occur in m · n ways."

     in our case, once we've met second 1
     2221221 - this even A and it can occur exactly four times
     1221
     21221
     221221
     2221221

    for each way of A events we exactly 4 ways when adding the rest twos after the second 1
    1221
    12212
    122122
    1221222

    for 2
    21221
    212212
    2122122
    21221222

    the same for 22, 222

    '''
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        evens = []
        count = res = 0
        for i in nums:
            if i % 2 == 0:
                count += 1
            else:
                evens.append(count)
                count = 0
        evens.append(count)
        for i in range(len(evens)-k):
            res += (evens[i]+1)*(evens[i+k]+1)
        return res

if __name__ == "__main__":
    s = Solution()
    s.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2)