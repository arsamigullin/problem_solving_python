# this problem
# https://leetcode.com/problems/brace-expansion/


class Solution:
    '''
    we use backtracking here
    '''
    def expand(self, S: str) -> List[str]:
        if not S:
            return S
        
        res = []
        def helper(i, word):
            if i >= len(S):
                return res.append(''.join(word))
            if S[i].isalpha():
                word.append(S[i])
                helper(i+1, word)
                word.pop()
            elif S[i] == '{':
                letters = []
                while S[i]!='}':
                    if S[i].isalpha():
                        letters.append(S[i])
                    i+=1
                for l in letters:
                    word.append(l)
                    helper(i+1,word)
                    word.pop()
        helper(0,[])
        return sorted(res)