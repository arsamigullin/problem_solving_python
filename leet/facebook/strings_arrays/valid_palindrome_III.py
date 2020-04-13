#this problem
#https://leetcode.com/problems/valid-palindrome-iii/

class Solution:
    '''
    we are given string, return True if removing at most k chars we can make a palindrome from string
    Algo:
    1. we find max palindrome from given string using longes_palindromic_subsequence.py technique
    2. if len(s) - (found max len of palindrome) <= k, return True 

    NOTE: helper returns max len of palindrome
    '''
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = {} 
        def helper(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if s[i] == s[j]:
                return helper(i+1, j-1) + 2
            key=f"{i}|{j}"
            if key not in dp:
                dp[key] = max(helper(i+1, j), helper(i, j-1))
            return dp[key]
        return k >= (len(s) - helper(0, len(s)-1)) 
            