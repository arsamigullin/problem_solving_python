def solution(H):
    # write your code in Python 3.6
    stack = []
    count = 0
    for index, value in enumerate(H):
        count += iter(value, stack)
    return count + len(stack)

def iter(value, stack):
    if len(stack) == 0:
        stack.append(value)
        return 0
    latest = stack[len(stack) - 1]
    if latest > value:
        stack.pop()
        return iter(value, stack) + 1
    elif latest == value:
        return 0
    else:
        stack.append(value)
        return 0


if __name__ == "__main__":
    data = [8, 8, 5, 7, 9, 9, 8, 8, 7, 4, 8]
    print(solution(data))