# O(n3) solution
def solutionOn3(A):
    max_sum = 0
    for p in range(len(A)):
        for q in range(p, len(A)):
            sum = 0
            for i in range(p, q + 1):
                sum += A[i]
            max_sum = max(max_sum, sum)
    return max_sum


# O(n2) with prefix sum
def solutionOn2_with_pref_sums(A):
    # calculate pref sums
    pref = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        pref[i] = pref[i - 1] +  A[i - 1]
    max_sum = 0
    for p in range(0, len(A)):
        for q in range(p+1, len(A)):
            max_sum = max(max_sum, pref[q] - pref[p])
    return max_sum

# solution On2 without prefix sums
def solutionOn2(A):
    max_sum = 0
    for p in range(0, len(A)):
        sum_slice = A[p]
        for q in range(p+1, len(A)):
            sum_slice += A[q]
            max_sum = max(sum_slice, max_sum)
    return max_sum

# solution O(N)
def solutionOn(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_ending

if __name__ == "__main__":
    #print(solutionOn([5, -7, 3, 5, -2, 4, -1]))
    #print(solutionOn2([5, -7, 3, 5, -2, 4, -1]))
    #print(solutionOn2_with_pref_sums([5, -7, 3, 5, -2, 4, -1]))
    #print(solutionOn3([5, -7, 3, 5, -2, 4, -1]))
    print(solutionOn([23171, 21011, 21123, 21366, 21013, 21367]))
