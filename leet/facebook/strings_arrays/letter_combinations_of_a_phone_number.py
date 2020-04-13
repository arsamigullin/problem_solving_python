# DFS
class MySolution:
    def letterCombinations(self, digits: str) -> list:
        d = {'1': "", '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz",
             '0': ""}

        def find(dig, i):
            if i >= len(digits):
                return []
            arr = find(dig, i + 1)
            s = d[dig[i]]
            if len(arr) == 0:
                return [c for c in s]
            res = []
            for ch in s:
                [res.append(ch + c) for c in arr]
            return res

        return find(digits, 0)


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])

        output = []
        if digits:
            backtrack("", digits)
        return output

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {'1':"", '2':"abc", '3':"def", '4':"ghi", '5':"jkl", '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz", '0':""}
        dp = [[] for _ in range(len(digits)+1)]
        dp[0].append('')
        for i in range(len(digits)):
            num = d[digits[i]]
            for s in dp[i]:
                for c in num:
                    dp[i+1].append(s+c)
        return dp[len(digits)]

# using itertools
# this is most fast solution 
class SolutionIt:
    def letterCombinations(self, digits: str) -> list:
        if not digits: return []

        REPS = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz", 0: " "}
        if len(digits) == 1: return [c for c in REPS[int(digits)]]

        pool = []
        for i in digits:
            pool.append(REPS[int(i)])

        from itertools import product
        return ["".join(prd) for prd in product(*pool)]
if __name__ == "__main__":
    s = SolutionIt()
    s.letterCombinations("234")