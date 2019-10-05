def findMaxLength(nums):
    count, max_len = 0, 0
    d = dict()
    for i in range(len(nums)):
        count = count + (1 if nums[i] == 1 else -1)
        if (count in d):
            max_len = max(max_len, i - d.get(count))
        else:
            d[count] = i
    return max_len

if __name__ == "__main__":
    findMaxLength([0,1,0,1])