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


class SolutionBelow:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

if __name__ == "__main__":
    print(SolutionMy(10))