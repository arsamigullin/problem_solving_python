# microsoft

# Suppose I had an array:
#
# [1, 8, 5, 6, 10, 9, 11, 12];
# I want to sort it by ascending order, but find out the maximum groups I would need to sort. In this example, the answer would be:
#
# [1], [8,5,6], [10,9], [11], [12]: so 5
# [3, 2, 1] would come out to be 1 because the entire array would need sorting.
#
# I am at a complete loss of how to do this a nudge in the right direction would be greatly appreciated.
# [1, 8, 5, 6, 10, 9, 11, 12];

class Solution:
    def solve(self, A):
        stack = [A[0]]
        for i in range(1, len(A)):
            if stack[-1]<=A[i]:
                stack.append(A[i])
            elif stack[-1] > A[i]:
                last = stack[-1]
                while stack and stack[-1] > A[i]:
                    stack.pop()
                stack.append(last)
        return len(stack)


if __name__ == '__main__':
    s = Solution()
    s.solve([8,5,6,12,11,13])
    s.solve([1,1,1,1,1,1])
    s.solve([1, 8, 5, 6, 10, 9, 11, 12])
