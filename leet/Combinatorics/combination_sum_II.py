class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list:
        candidates.sort()
        result = []
        combinations = []
        def find_combinations(i, t):
            nonlocal result
            nonlocal combinations
            if t == 0:
                result.append(combinations[:])
                return
            prev = -1
            for j in range(i, len(candidates)):
                if prev == candidates[j]:
                    continue
                new_target = t - candidates[j]
                if new_target<0:
                    break
                else:
                    combinations.append(candidates[j])
                    find_combinations(j+1, new_target)
                    prev = combinations.pop()

        find_combinations(0, target)
        return result

if __name__ == "__main__":
    s = Solution()
    #s.combinationSum2([10,1,2,7,6,1,5], 8)
    s.combinationSum2([2,5,2,1,2], 5)