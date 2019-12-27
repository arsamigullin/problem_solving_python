#Intuition
#The words are sorted lexicographically if and only if adjacent words are.
# This is because order is transitive: a <= b and b <= c implies a <= c.
#Algorithm
#Let's check whether all adjacent words a and b have a <= b.
#To check whether a <= b for two adjacent words a and b,
# we can find their first difference. For example, "applying" and "apples"
# have a first difference of y vs e. After, we compare these characters
# to the index in order.
#Care must be taken to deal with the blank character effectively.
# If for example, we are comparing "app" to "apply",
# this is a first difference of (null) vs "l".

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        omap = {v: i for i, v in enumerate(order)}

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            no_dif = True
            for j in range(min(len(w1), len(w2))):
                if omap[w1[j]] != omap[w2[j]]:
                    if omap[w1[j]] > omap[w2[j]]:
                        return False
                    no_dif = False
                    break
            if no_dif:
                if len(w1) > len(w2):
                    return False

        return True
