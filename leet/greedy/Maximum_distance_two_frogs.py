# microsoft

# Frog Jumps
#There are N block from 0 to N-1. A couple of frogs were sitting together on one block, They had a quarrel and need to jump away from one another.
# The frogs can only jump to another block if the height of the other block is greater than equal to the current one. You need to find the longest possible
# distance that they can possible create between each other, if they also choose to sit on an optimal starting block initially.
#
# Frogs can only jump on higher value elements or some of the same height and they can not skip any elements.
#
# Input: [1, 5, 5, 2, 6]
#
# Output: 3. Largest distance of 3 is created by having spawn location 3 (0-indexed) and left frog jump until
# index 1 and right frog jumps until index 4.
#
# len(input_array) is between 2 and 200 000. Values in array are integers between 1 and 1 000 000 000.
from typing import List


class Solution:
    def find(self, A):
        prev_top = 0
        is_going_up = False
        res = 0
        repeated = 0
        cur_top = 0
        for i in range(len(A)-1):
            # started going up
            if A[i] <= A[i+1]:
                cur_top = i + 1
                if A[i] == A[i+1]:
                    repeated += 1
                else:
                    is_going_up = True
                    repeated = 0
            # started going down
            else:
                # if it was going up
                if is_going_up:
                    # this is only to cover case [5 5 5 2 1]
                    prev_top = cur_top - repeated
                    is_going_up = False
                    repeated = 0
                cur_top = i + 1
            res = max(res, cur_top - prev_top + 1)
        return res

    def one_pass_solution(self, array: List[int]) -> int:
        current_peak_index = 0
        previous_peak_index = 0
        repeat_peaks = 0
        max_distance = 0
        is_going_up = False
        for i in range(len(array) - 1):
            this_height, next_height = array[i], array[i + 1]
            # started going up
            if next_height >= this_height:
                current_peak_index = i + 1
                if next_height == this_height:
                    repeat_peaks += 1
                else:
                    is_going_up = True
                    repeat_peaks = 0
            # started going down
            else:
                # if it was going up before
                if is_going_up:
                    previous_peak_index = current_peak_index - repeat_peaks
                    is_going_up = False
                    repeat_peaks = 0
                current_peak_index = i + 1
            max_distance = max(max_distance, current_peak_index - previous_peak_index + 1)

        return max_distance

if __name__ == '__main__':
    s = Solution()
    print(s.find([3,2,1,1,2,3]))  #
    print(s.find([4, 4, 1, 1, 1]))  #
    print(s.find([1, 1, 1, 4, 4]))  # 4
    print(s.find([1,1,1,3,1])) # 4, when it reaches 3 the repeated is reset
    print(s.find([5,4,3,3,3,3,2,1])) # 8
    print(s.find([1,2,3,3,3,3,4,5])) # 8
    print(s.find([1,5,5,2,6])) # 4
    print(s.find([5,5,5,4,3,2,3,4,5])) # 9

    print(s.one_pass_solution([5,4,3,3,3,3,2,1])) # 8
    print(s.one_pass_solution([1,2,3,3,3,3,4,5])) # 8
    print(s.one_pass_solution([1,5,5,2,6])) # 4
    print(s.one_pass_solution([5,5,5,4,3,2,3,4,5])) # 9



