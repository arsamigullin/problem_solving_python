# this problem
# https://leetcode.com/problems/unique-binary-search-trees/
# dynamic programming
# binary search trees


class SolutionMy:
    '''
    the idea is to pick the root (i) and multiply combinations on the left subtree and
    combinations on the right subtree
    NOTE: If count of nodes on the left and right subtrees not equal this means
    we can just double the product of combinations of left and right subtrees
    '''
    def numTrees(self, n: int) -> int:
        d = {0:1, 1:1, 2:2}
        for i in range(3, n + 1):
            half = (i//2 + i%2)+1
            cnt = 0
            for j in range(1, half):

                l = j - 1
                r = i - j
                # if l and r are equal this means the current root i has equal nodes in the left subtree
                # and in the right subtree
                # in this case we should multiply to two since they will be structurally the same
                # but if l and r not equal we must multiply on two their product
                # since we can swap left and right subtrees and we will get structurally different trees
                combcnt = d[l] * d[r]
                if l != r:
                    combcnt*=2 # because of this two I reduce the iterations of the internal array
                               # otherwise we would need to go over the whole array as it is done in the solution below
                cnt+=combcnt
            d[i]=cnt
        return d[n]

# Catalan Numbers
class Solution:
    def numTrees(self, n: int) -> int:

        if n <= 0:
            return 1
        C = 1
        for i in range(n):
            C = C * (2 + 4 * i) / (2 + i)

        return int(C)



class SolutionBelow:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        # In mathematics, the Cartesian product is a binary operation that takes two sets and returns a new set consisting of all possible ordered pairs

        # we explore every possible number of nodes in the tree starting from 2
        for i in range(2, n+1):
            # here j is the root of the tree
            # G[j-1] is the number of unique subtrees of the left subtree with root j
            # G[i-j] is the number of unique subtrees of the right subtree with root j
            # here we do cartesian product because on the left side of the root j we have number of unique combinations
            # the same on the right side. So, doing cartesian product gives total possible combinations
            print(f"i={i}")
            # from the given number of nodes of the tree, i.e. i in this case
            # we pick up the root node with value in it equal j
            # again, G contains NUMBER of unique subtrees where INDEX means the total number of nodes in that subtree
            # i.e. G[i] the number of unique subtrees when total nodes count is i
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]
                print(f"{j-1} {j} {i-j}")
                # let's say i = 5
                #i=5
                #j-1  j   i-j
                #0    1    4
                #1    2    3
                #2    3    2
                #3    4    1
                #4    5    0
                # i-j is to alternate j-1 and i-j around j
            print("############")

        return G[n]

if __name__ == "__main__":
    s = SolutionBelow()
    print(s.numTrees(7))