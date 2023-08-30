# monotonous stack
# this is to find next greater items of the given array
# for nums array the result is
# [5,6,6,18,-1,-1]

def next_greater(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            index = stack.pop()
            result[index] = arr[i]
        stack.append(i)
    return result

if __name__ == '__main__':
    next_greater([1,5,3,6,18,6])