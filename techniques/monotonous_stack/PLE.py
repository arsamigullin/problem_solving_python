# this monotonous technique helps to find Previous Less Element (PLE)
def find_ple(arr):
    stack = []
    previous_less = [0] * len(arr)
    for i in range(len(arr)):
        while len(stack) > 0 and stack[-1] > arr[i]:
            stack.pop()
        previous_less[i] = stack[-1] if len(stack) > 0 else -1
        stack.append(arr[i])
#The previous less element of 7 is 3.
#The previous less element of 8 is 7.
#The previous less element of 4 is 3.
if __name__ == "__main__":
    find_ple([3,7,8,4]) # previous_less = [-1,3,7,3]