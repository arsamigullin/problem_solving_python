class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        # this dict if for center numbers. For example, we can draw 1->2->3 line
        # but we also can draw 1->3 line if and only if 2 was previously used
        # and to check if 2 was in use, we are going to check pairs that consitutes the current line ( 1 and 3 in our case)
        exceptions = {(1, 3): 2, (3, 1): 2, (1, 7): 4, (7, 1): 4, (3, 9): 6, (9, 3): 6, (7, 9): 8, (9, 7): 8, (1, 9): 5,
                      (9, 1): 5, (3, 7): 5, (7, 3): 5, (4, 6): 5, (6, 4): 5, (2, 8): 5, (8, 2): 5}

        memo = {}

        def get_count_of_unlock_patterns(curr, start, visited):
            if start > n:
                return 0
            if (curr, start, visited) not in memo:
                ans = 0
                if start >= m:
                    ans = 1
                for next_num in range(1, 10):
                    # if curr equals next_num or next_num is already visited or the current pair is in exceptions and
                    # the center number has not been visited yet
                    if next_num == curr or (visited & (1 << next_num)) > 0 or (
                            (curr, next_num) in exceptions and (visited & (1 << exceptions[(curr, next_num)]) == 0)):
                        continue
                    ans += get_count_of_unlock_patterns(next_num, start + 1, visited | (1 << next_num))
                memo[(curr, start, visited)] = ans
            return memo[(curr, start, visited)]

        return sum(get_count_of_unlock_patterns(i, 1, 1 << i) for i in range(1, 10))