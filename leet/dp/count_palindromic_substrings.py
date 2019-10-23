def bruteForce(S):
    N = len(S)
    ans = 0
    for center in range(2 * N - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < N and S[left] == S[right]:
            ans += 1
            left -= 1
            right += 1
    return ans


def usingDpApproach(S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in range(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1 # increase a palindrome length with center i

            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z
    z = manachers(S)
    return sum((v+1)/2 for v in z)


def countSubstrings(S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A) # this an array where index denotes the index center of palindrome in string s and value is
        # length of that palindrome
        center = right = 0
        for i in range(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z

    return sum((v+1)//2 for v in manachers(S))

if __name__ == "__main__":
    print(countSubstrings("zpaaaarg"))
    #print(usingDpApproach("aabcba"))
