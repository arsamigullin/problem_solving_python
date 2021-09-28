# this is the first solution
# public int hammingWeight(int n) {
#     int sum = 0;
#     while (n != 0) {
#         sum++;
#         n &= (n - 1);
#     }
#     return sum;
# }

class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        while n != 0:
            lsone = n & (-n)
            n^=lsone
            cnt+=1
        return cnt

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n!=0:
            count+=1
            n&=n-1
        return count
