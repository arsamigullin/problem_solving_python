def solution(A):
    # let's determine a leader
    size = 0
    for i in A:
        if size == 0:
            size += 1
            value = i
        else:
            if value == i:
                size += 1
            else:
                size -= 1
    if size <= 0:
        return 0

    count = 0
    for i in A:
        if value == i:
            count += 1

    # make sure if the found value is really leader
    if count > len(A) // 2:
        total_cnt = 0
        lenght = len(A)
        lead_cnt = 0
        index_cnt = 0
        for i in A:
            total_cnt += 1
            if i == value:
                lead_cnt += 1
            if lead_cnt > total_cnt // 2 and (count - lead_cnt) > (lenght - total_cnt) // 2:
                index_cnt += 1
        return index_cnt
    else:
        return 0

if __name__ == "__main__":
    print(solution([4, 3, 4, 4, 4, 2] ))
    #print(solution([4, 4, 2, 5, 3, 4, 4, 4]))
    #print(solution([-1000000000, -1000000000]))