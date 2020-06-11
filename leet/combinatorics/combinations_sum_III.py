class Solution:
    def combinationSum3(self, k: int, n: int) -> list:
        result = []
        def find(i, t, combinations):
            nonlocal result
            if len(combinations) == k and t == 0:
                result.append(combinations[:])
                return
            for j in range(i, 10):
                new_target = t - j
                if new_target < 0:
                    break
                if len(combinations)>=k:
                    break
                combinations.append(j)
                find(j+1,new_target, combinations)
                combinations.pop()
        find(1, n, [])
        return result

if __name__ == "__main__":
    s = Solution()
    s.combinationSum3(3,7)