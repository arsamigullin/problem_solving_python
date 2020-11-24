import typing
List = typing.List

class SolutionShort:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        consider example
        [1,2,3,4,5,6]
        k = 2
        n = 6
        NOTE: n-k elments will necessary go to the beginning of k elements
        nums[:2], nums[2:] = nums[4:], nums[:4],
        """
        n = len(nums)
        k = k % n
        nums[:k], nums[k:] = nums[n - k:], nums[:n - k]


class SolutionRev:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # reverse whole array
        nums[0:] = nums[::-1]
        # reverse first k elements
        nums[:k] = nums[:k][::-1]
        # reverse rest element starting from k
        nums[k:] = nums[k:][::-1]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k = k % n
        cnt = 0
        i = 0
        while cnt < n:
            cur = i
            prev = nums[i]
            while True:
                nxt = (cur + k) % n
                prev, nums[nxt] = nums[nxt], prev
                cur = nxt
                cnt += 1
                # if we reached the index we started from (this means we looped)
                # break
                if i == cur:
                    break
            # start with the next index
            i += 1

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        val = nums[0]
        start = 0
        i = k
        for _ in range(n):
            # if the pointer returns to the place it started
            # we do not need to do a swap
            # we just assign the value
            if i == start:
                nums[i] = val
                # and increment i not to loop over the nums
                i+=1
                start = i
                # this is to avoid indexoutofrange
                val = nums[i%n]
            else:
                # do just a swap
                nums[i], val = val, nums[i]
            i=(k+i)%n
        return nums

if __name__ == "__main__":
    s = Solution()
    s.rotate([1,2,3,4,5,6,7],2)

