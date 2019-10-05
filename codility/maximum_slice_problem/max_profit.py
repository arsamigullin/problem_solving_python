def solution(A):
    max_profit = profit = 0
    min_price = 200001
    for a in A:
        min_price = min(min_price, a)
        profit = max(0, a - min_price)
        max_profit = max(max_profit, profit)
    return max_profit

def solution1(A):
    # write your code in Python 3.6
    max_profit = 0
    for p in range(len(A)):
        for q in range(p + 1, len(A)):
            max_profit = max(max_profit, A[q] - A[p])
    return max_profit

if __name__ == "__main__":
    print(solution([23171, 21011, 21123, 21366, 21013, 21367]))