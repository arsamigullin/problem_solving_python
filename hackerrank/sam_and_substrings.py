# let's suppose the input string is 1234
# this table shows where each digit is met
# table
#      1000    100    10    1
# 1       1      1     1    1
# 2              1     1    1
# 3                    1    1
# 4                         1

# this table helps us to determine weight coef (mul_ten)
# the solution spinning around this formula
# value added by si = si SUM(10^i, where i is 0 ... n-1) * (i+1)


def solution(s):
    len1 = len(s)
    mul_ten = 1 # value from table
    sum1 = 1 # summation SUM above
    total_sum = len1 * int(s[len1 - 1])
    for i in range(len1 - 2, -1, -1):
        mul_ten = (mul_ten * 10) % 1000000007
        sum1 = sum1 + mul_ten
        total_sum = (total_sum + (sum1 * (i + 1)) * int(s[i])) % 1000000007
    return total_sum % 1000000007

if __name__ == "__main__":
    print(solution('1234'))