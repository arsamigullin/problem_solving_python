class Solution:
    def get_permutations(self,s,k):
        res = []
        def find(arr, permutations, k):
            if k <= 0:
                res.append(permutations[:])
                return
            for j, el in enumerate(arr):
                permutations.append(el)
                if k > 0:
                    find(arr[:j] + arr[j+1:], permutations, k - 1)
                permutations.pop()
        find(s,[], k)
        print(res)
if __name__ == "__main__":
    s = Solution()
    s.get_permutations("abcd", 1)



