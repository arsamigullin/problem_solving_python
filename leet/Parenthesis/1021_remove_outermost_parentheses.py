class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        balance = 0
        indexes = []
        # once we reached balance = 0, we got primitive
        # fix its start and end index
        for i, brace in enumerate(S):
            if brace == '(':
                if balance == 0:
                    indexes.append(i)
                balance += 1
            else:
                balance -= 1
                if balance == 0:
                    indexes.append(i)
        result = []
        # cut out outer parenthesis according to indexes array
        for i in range(0, len(indexes), 2):
            s = indexes[i]
            e = indexes[i + 1]
            result.append(S[s + 1:e])
        return ''.join(result)
