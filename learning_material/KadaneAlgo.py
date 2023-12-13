def kadane(gen):
    # Maximum non-empty subarray sum
    ans = cur = - 10**6
    for x in gen:
        cur = x + max(cur, 0)
        ans = max(ans, cur)
    return ans

if __name__ == '__main__':
    kadane([-3,-1,-2])