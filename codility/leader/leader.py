def goldenLeader(A):
    n = len(A)
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in range(n):
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
        leader = candidate
    return leader

def goldenLeader2(H):
    stack = []
    for i, v in enumerate(H):
        if len(stack) == 0:
            stack.append(v)
        else:
            latest = stack[len(stack) - 1]
            if latest == v:
                stack.append(v)
            else:
                stack.pop()
    candidate = -1
    if len(stack) > 0:
        candidate = stack.pop()
    count = 0
    for i in range(len(H)):
        if candidate == H[i]:
            count += 1
    if count > len(H)//2:
        return candidate
    return -1



if __name__ == "__main__":
    print(goldenLeader2([6, 8, 4, 6, 8, 6, 6]))
    #print(goldenLeader2([4,6,6,6,6,8,8]))