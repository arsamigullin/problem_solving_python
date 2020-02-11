class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: int, k: int) -> list:

        def find(n, k, i, combinations):
            if k == 0:
                self.res.append(combinations[:])
                return
            for j in range(i, n + 1):
                if k > 0:
                    combinations.append(j)
                    find(n, k - 1, j + 1, combinations)
                    combinations.pop()

        find(n, k, 1, [])
        return self.res


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k:
            return []

        combinations = []

        def combine(index, combination):
            # Base case - combination contains k characters
            if len(combination) == k:
                combinations.append(combination[:])
                return

            # Recursive case - consider every combination
            for number in range(index, n + 1):
                # Abort if there aren't enough numbers remaining to
                #   make a valid combination
                if (len(combination) + (n - number + 1)) < k:
                    break

                # Add number, recurse, and backtrack
                combination.append(number)
                combine(number + 1, combination)
                combination.pop()

        combine(1, [])
        return combinations


class Solution:
    def combine(self, n: int, k: int) -> list:
        from itertools import combinations
        return [*combinations([i for i in range(1, n + 1)], k)]

if __name__ == "__main__":
    s = Solution()
    s.get_permutations("abcd", 2)



