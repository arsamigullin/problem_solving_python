class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        results = []
        candidates.sort()

        def find(i, diff, combinations):
            nonlocal results
            if diff == 0:
                results.append(combinations[:])
                return
            if diff < 0:
                return
            for j in range(i, len(candidates)):
                if diff - candidates[j] < 0:
                    break
                combinations.append(candidates[j])
                find(j, diff - candidates[j], combinations)
                combinations.pop()

        find(0, target, [])
        return results
