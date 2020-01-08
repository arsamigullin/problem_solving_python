# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class SolutionMy:
    def __init__(self):
        self.depth = 0
        self.d = {}

    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def find_depth(nestedList, depth):
            for l in nestedList:
                if l.isInteger():
                    self.d[depth] = self.d.get(depth, 0) + l.getInteger()
                    self.depth = max(self.depth, depth)
                else:
                    find_depth(l.getList(), depth + 1)

        find_depth(nestedList, 1)
        return sum(abs(k - self.depth - 1) * v for k, v in self.d.items())

# very interesting solution
# Note we do not reset leve_sum after adding up to the total_sum
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        total_sum = level_sum = 0
        while nestedList:
            nxt_level_list = []
            for ele in nestedList:
                if ele.isInteger():
                    level_sum += ele.getInteger()
                else:
                    nxt_level_list += ele.getList()
            total_sum += level_sum
            nestedList = nxt_level_list
        return total_sum