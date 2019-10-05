def solution(nums):
    v = 0
    for i in range(len(nums)):
        v = v^nums[i]
    print(v)

if __name__ == "__main__":
    solution([2,1,2,1])