# IDEA :
# If we know what is super palindrome then we can easily solve this problem
#
# So What is Super palindrome??
# A super palindrome number is a palindrome number whose square is also a palindrome.
#
# For example:
# Consider a number 11 and the square of the number is 121 which is also a palindrome.
#
# So, what logic I have used here:
# 2+2(string addition) => 22 * 22 = 484 which is also a palindrome.
#
# Most of you will have one more question Why I have used odd length and even length palindromes.
# Let's assume a number 1234 with this number we can form two palindromes
#
# Odd Length Palindrome 1234321(reverse the given number and add to it by ignoring the 1st character)
# Even Length Palindrome 12344321 (simply reversing the given number and add to it)
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:

        left = int(left)
        right = int(right)
        limit = 100000
        c = 0

        def is_pal(num):
            return str(num) == str(num)[::-1]

        # For even length palindrome
        for i in range(limit):
            s = str(i)
            s = s + s[::-1]
            p = int(s)
            p2 = p ** 2
            if p2 > right:
                break
            if p2 > left and is_pal(p2):
                c += 1

        # For odd length palindrome
        for i in range(1, limit):
            s = str(i)
            s = s + s[::-1][1:]
            p = int(s)
            p2 = p ** 2
            if p2 > right:
                break
            if p2 >= left and is_pal(p2):
                c += 1

        return c