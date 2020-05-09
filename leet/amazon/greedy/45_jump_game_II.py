from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        let's consider an array
        [2,3,1,1,4,2,3,1] values
        [0,1,2,3,4,5,6,7] indexes
        initially next_max_steps and max_steps are equal 2
        max_steps is maximum steps we can jump from the latest point
        next_max_steps - once max_steps are exhausted we continue moving further
        putting next_max_steps
        since there possible to pass the point which brings farthest distance to jump
        (for example, nums[1] + 1 = 4, from index 1 we can jump further than from index 0
        we keep track for that distance to continue jumping once max_steps are exhausted
        substituting max_steps with nex_max_steps  once max_steps exhausted
        we continue to track the next next_max_step

        The greedy thing here is we want to exhaust curren max_steps

        starting from index 1 we check if the current index is greater that max_steps
        '''

        n = len(nums)
        if n < 2:
            return 0


            # max position one could reach
        # starting from index <= i
        next_max_steps = nums[0]
        # max number of steps one could do
        # inside this jump
        max_steps = nums[0]

        jumps = 1
        for i in range(1, n):
            # if to reach this point
            # one needs one more jump

            if max_steps < i:
                jumps += 1
                max_steps = next_max_steps
            next_max_steps = max(next_max_steps, nums[i] + i)

        return jumps

if __name__ == '__main__':
    s = Solution()
    s.jump([2,3,1,1,4])

