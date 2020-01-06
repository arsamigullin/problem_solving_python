# this monotonous technique helps to find Next Less Element (PLE)
# instead of storing the value itself we will store the index-
def find_nle(arr):
    stack = []
    next_less = [-1] * len(arr)
    for i in range(len(arr)):
        while len(stack) > 0 and arr[stack[-1]] > arr[i]:
            next_less[stack.pop()] = i
        stack.append(i)
#The next less element of 7 is 3.
#The next less element of 8 is 3.
#No next less element of 4 and 3.
if __name__ == "__main__":
    find_nle([3,7,8,4]) # next_less = [-1,3,3,-1] this is an array with indices