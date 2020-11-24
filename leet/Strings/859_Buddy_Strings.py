class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        cnt = 0
        can = False
        d = {}
        for ch in A:
            d[ch] = d.get(ch, 0) + 1
            # having at least two the same characters, allows us to do a swap
            if d[ch] >= 2:
                can = True

        for a, b in zip(A, B):
            if a != b:
                if b in d:
                    d[b] -= 1
                    if d[b] == 0:
                        d.pop(b)
                else:
                    # if not char from b is in A
                    return False
                cnt += 1
                # if we have more than two inequalities
                # it will not be possible to
                if cnt > 2:
                    return False

        return cnt == 2 or can
