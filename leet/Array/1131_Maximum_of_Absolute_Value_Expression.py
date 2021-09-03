# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# we can get rid of abs
# if we know for sure that i>j and x>y
# but the problem is we do not know what is greater
# try
def mfdm(i, j, x,y):
    a = abs(i - j) + abs(x - y)
    b = (i - j ) + (x - y)
    c = (i + x) - (j + y)
    d = (i - j ) - (x - y)
    e = (i - x) - (j - y)
    f =-(i - j ) + (x - y)
    g = (-i + x) - (-j + y)
    h = -(i - j ) - (x - y) # -(2-3)-(5-6)= -2+3+6-5=1+1=2
    i = (-i - x) - (-j - y) # (2,3,5,6) (-2-5) - (-3-6) = -7 + 9
    # a = (x_i + y_i) - (x_j + y_j)
    # b = (x_i - y_i) - (x_j - y_j)
    # c = (-x_i + y_i) - (-x_j + y_j)
    # d = (-x_i - y_i) - (-x_j - y_j)

    print(a,b,c,d,e,f,g,h,i)


# // The given expression: |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# // How to remove the absolute operator: we can compute the absolute difference between two variables without the absolute operator if we know which one is greater or equal. So if a <= b, then |a - b| == b - a.
# // So we want to compute the expression for all combinations of i and j such that i <= j. To compute the expression without the absolute operator, we need to try out all four cases:
# // First case:  arr1[i] <= arr1[j] && arr2[i] <= arr2[j]  -->  arr1[j] - arr1[i] + arr2[j] - arr2[i] + j - i  ==  (arr1[j] + arr2[j] + j) + (-arr1[i] - arr2[i] - i).
# // Second case: arr1[i] <= arr1[j] && arr2[i] >= arr2[j]  -->  arr1[j] - arr1[i] + arr2[i] - arr2[j] + j - i  ==  (arr1[j] - arr2[j] + j) + (-arr1[i] + arr2[i] - i).
# // Third case:  arr1[i] >= arr1[j] && arr2[i] <= arr2[j]  -->  arr1[i] - arr1[j] + arr2[j] - arr2[i] + j - i  ==  (-arr1[j] + arr2[j] + j) + (arr1[i] - arr2[i] - i).
# // Fourth case: arr1[i] >= arr1[j] && arr2[i] >= arr2[j]  -->  arr1[i] - arr1[j] + arr2[i] - arr2[j] + j - i  ==  (-arr1[j] - arr2[j] + j) + (arr1[i] + arr2[i] - i).
# // How to compute the maximum of these expressions in one pass: similar to "best time to buy and sell stock" problem, we maintain the minimum as we go (best past value that we can combine future values with) and we compute the max value that the current value can achieve by combining it with the best previous value. Only difference between "best time to buy and sell stock" and this problem, is that we have more cases here.


#https://leetcode.com/problems/maximum-of-absolute-value-expression/discuss/339968/JavaC%2B%2BPython-Maximum-Manhattan-Distance
#!!!!!!!!!!!!!IMPORTANT TO UNDERSTAND HERE#################################
# So we can see, the expression
# |x[i] - x[j]| + |y[i] - y[j]| + |i - j| = f(j) - f(i)
#
# where f(i) = p * x[i] + q * y[i] + i
# with p = 1 or -1, q = 1 or -1

def maxAbsValExpr(x, y):
    res, n = 0, len(x)
    # so we do not calculate this |x[i] - x[j]| + |y[i] - y[j]| + |i - j| directly
    # rather decompose it and try different options
    # as been shown by lee
    # | x[i] - x[j] | + | y[i] - y[j] | = (x[i] - x[j]) + (y[i] - y[j]) = (x[i] + y[i] |) - (x[j] + y[j])
    # | x[i] - x[j] | + | y[i] - y[j] | = (x[i] - x[j]) - (y[i] - y[j]) = (x[i] - y[i] |) - (x[j] - y[j])
    # | x[i] - x[j] | + | y[i] - y[j] | = -(x[i] - x[j]) + (y[i] - y[j]) = (-x[i] + y[i] |) - (-x[j] + y[j])
    # | x[i] - x[j] | + | y[i] - y[j] | = -(x[i] - x[j]) - (y[i] - y[j]) = (-x[i] - y[i] |) - (-x[j] - y[j])

    # we can get rid of abs
    # if we know for sure that x[i]>x[j] and y[i]>y[j]
    # but the problem is we do not know what is greater

    # and since we do not calculate this |x[i] - x[j]| + |y[i] - y[j]| + |i - j| directly
    # we try different option, so eventually, it will result in max result, as if we calculated that formula directly
    for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
        smallest = p * x[0] + q * y[0] + 0 # f(i)
        for i in range(n):
            cur = p * x[i] + q * y[i] + i # f(j)
            res = max(res, cur - smallest) # f(j) - f(i)
            smallest = min(smallest, cur)
        print(res)
    return res

if __name__ == '__main__':
    mfdm(1,2,3,4)
    maxAbsValExpr([1,2,3,4],[4,3,2,1])
    mfdm(2,3,5,6)