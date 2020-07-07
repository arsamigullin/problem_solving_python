def somefun(arr1, arr2):
    res = []
    for i in range(len(arr1)):
        twosum = arr1[i] + arr2[i]
        res.append(twosum+3*(twosum%2))
    return res

if __name__ == '__main__':
    a = [0, 1, 2, 3, 4]
    b = [5, 6, 7, 8, 9]
    somefun(a,b)

[8,10,12,14,16]