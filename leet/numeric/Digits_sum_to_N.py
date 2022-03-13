# microsoft
# Given an integer N, return the smallest non-negative number whose individual digits sum upto N.
# An efficient approach to this problem is an observation. Let’s see some examples.
# If N = 10, then ans = 19
# If N = 20, then ans = 299
# If N = 30, then ans = 3999
# So, it is clear that the answer will have all digits as 9 except the first one so that we get the smallest number.
def solution():
    N = 315
    res = (N % 9 + 1) * pow(10, N // 9) - 1

    print(res)

if __name__ == '__main__':
    solution()
    print('Done')