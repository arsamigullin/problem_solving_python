def solution(n):
    total = 0
    prev2= 0
    prev1 = 1
    for i in range(n-2):
        total = prev1 + prev2
        prev2, prev1 = prev1, total
    return total

if __name__ == "__main__":
    print(solution(8))
