# Algo
# if char is numeric
# just got to the next char
# otherwise we want to transform
class Solution:
    def letterCasePermutation(self, S: str) -> list:
        res = []
        arr = list(S)
        print(arr)

        def permute(i):
            if i == len(S):
                res.append(''.join(arr))
                return
            if arr[i].isnumeric():
                permute(i+1)
            else:
                arr[i] = arr[i].upper() if arr[i].islower() else arr[i].lower()
                permute(i+1)
                arr[i] = arr[i].upper() if arr[i].islower() else arr[i].lower()
                permute(i + 1)


        permute(0)
        return res

# for each item in result set
# we change case
class SolutionExtend:
    def letterCasePermutation(self, S: str) -> list:
        res = [S.lower()]
        for i, c in enumerate(S.lower()):
            if c.isalpha():
                rlist = []
                for s in res:
                    rlist.append(s[:i] + c.upper() + s[i+1:])
                res.extend(rlist)
                #res.extend([s[:i] + c.upper() + s[i+1:] for s in res])
        return res

if __name__ == "__main__":
    s = SolutionExtend()
    s.letterCasePermutation("a1b2")
    s = Solution()
    s.letterCasePermutation2("a1b2")