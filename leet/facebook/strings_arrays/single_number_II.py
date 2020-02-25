import typing
List = typing.List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0

        for num in nums:
            # first appearance:
            # add num to seen_once
            # don't add to seen_twice because of presence in seen_once

            # second appearance:
            # remove num from seen_once
            # add num to seen_twice

            # third appearance:
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once

    def option2(self, nums: List[int]):
        check = []

        for i in nums:
            if (check.count(i) == 2):
                check.remove(i)
                check.remove(i)
            else:
                check.append(i)

        return check[0]

if __name__ == "__main__":
    s = Solution()
    s.singleNumber([4,3,4,3,4,3,99])
