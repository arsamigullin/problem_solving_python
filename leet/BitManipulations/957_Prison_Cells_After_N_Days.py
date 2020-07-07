from typing import List

# Complexity analisys
# let K be number of cells
# since this a bit string the, the max number of combinations is 2**K
# the overall complexity is K * min(2**K, N)

class SolutionTheSameAsBelow:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        seen = dict()
        is_fast_forwarded = False
        while N > 0:
            if not is_fast_forwarded:
                states = tuple(cells)
                if states in seen:
                    N %= seen[states] - N
                    is_fast_forwarded = True
                else:
                    seen[states] = N

            if N > 0:
                N -= 1
                cells = self.next_cells(cells)
        return cells

    def next_cells(self, cells):
        res = [0]
        for i in range(1, len(cells) - 1):
            res.append(int(cells[i - 1] == cells[i + 1]))
        res.append(0)
        return res

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        # seen is a dict where key is cells' state and value is day when this cells had these state
        # in other words dict says at which day (value) cells had these states (key)
        seen = dict()
        is_fast_forwarded = False

        while N > 0:
            # we only need to run the fast-forward once at most
            if not is_fast_forwarded:
                state_key = tuple(cells)
                if state_key in seen:
                    # the length of the cycle is seen[state_key] - N
                    N %= seen[state_key] - N
                    is_fast_forwarded = True
                else:
                    seen[state_key] = N

            # check if there is still some steps remained,
            # with or without the fast-forwarding.
            if N > 0:
                N -= 1
                next_day_cells = self.nextDay(cells)
                cells = next_day_cells

        return cells


    def nextDay(self, cells: List[int]):
        ret = [0]      # head
        for i in range(1, len(cells)-1):
            ret.append(int(cells[i-1] == cells[i+1]))
        ret.append(0)  # tail
        return ret

# Bit manipulation
class SolutionBitManipulation:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        seen = dict()
        is_fast_forwarded = False

        # step 1). convert the cells to bitmap
        state_bitmap = 0x0
        for cell in cells:
            state_bitmap <<= 1
            state_bitmap = (state_bitmap | cell)

        # step 2). run the simulation with hashmap
        while N > 0:
            if not is_fast_forwarded:
                if state_bitmap in seen:
                    # the length of the cycle is seen[state_key] - N
                    N %= seen[state_bitmap] - N
                    is_fast_forwarded = True
                else:
                    seen[state_bitmap] = N
            # if there is still some steps remained,
            #   with or without the fast-forwarding.
            if N > 0:
                N -= 1
                state_bitmap = self.nextDay(state_bitmap)

        # step 3). convert the bitmap back to the state cells
        ret = []
        for i in range(len(cells)):
            ret.append(state_bitmap & 0x1)
            state_bitmap = state_bitmap >> 1

        return reversed(ret)


    def nextDay(self, state_bitmap: int):
        state_bitmap = ~ (state_bitmap << 1) ^ (state_bitmap >> 1)
        state_bitmap = state_bitmap & 0x7e  # set head and tail to zero
        return state_bitmap

if __name__ == '__main__':
    s = SolutionBitManipulation()
    s.prisonAfterNDays([0,1,0,1,1,0,0,1],25)