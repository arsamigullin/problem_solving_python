# microsoft

# Write a function that, given an array A of N integers, returns the lagest integer K > 0 such that both values K and -K exist in array A.
# If there is no such integer, the function should return 0.
#
# Example 1:
#
# Input: [3, 2, -2, 5, -3]
# Output: 3
# Example 2:
#
# Input: [1, 2, 3, -4]
# Output: 0

def solution(arr):
    arr = sorted(arr)
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == 0:
            return arr[j]
        elif abs(arr[i]) > arr[j]:
            i += 1
        elif abs(arr[i]) < arr[j]:
            j -= 1
    return 0


print(solution([3, 2, -2, 5, -3]))