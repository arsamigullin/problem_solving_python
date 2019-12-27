import collections

from trees_and_graphs.dfs import TreeNode
#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# we use BFS
# we do not maintain a dictionary, instead we maintain local variable to store the sum at a particular level
# adding the nodes which is not None and using tuples instead of list for queue speeds up algo

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = collections.deque([(root, 1)])
        prev_level = 0
        smallest_level = 1
        max_val = root.val
        level_sum = root.val
        while len(queue) > 0:
            node, level = queue.popleft()
            if level != prev_level:
                if level_sum > max_val:
                    smallest_level = prev_level
                    max_val = level_sum
                level_sum = 0
                prev_level = level
            level_sum += node.val
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        if level_sum > max_val:
            smallest_level = prev_level

        return smallest_level

# this is quite interesting solution as well
# here we introduce marker. Once marker reached analyze current curr_sum and cur_level
# the queue will always contain marker element at the end therefore we in the while len(queue) > 1
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        cur_level = max_level = 1
        max_sum = float('-inf')
        curr_sum = 0
        marker = None
        queue = collections.deque([root, marker])

        while len(queue) > 1:
            node = queue.popleft()
            if node == marker:
                if curr_sum > max_sum:
                    max_sum = curr_sum
                    max_level = cur_level
                curr_sum = 0
                cur_level += 1
                queue.append(marker)
            else:
                curr_sum += node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return max_level

# short python solution
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        curr_level = max_level = 1
        max_sum = float('-inf')
        queue = [root, ]

        while queue:
            # sum up all the nodes on the current level
            curr_sum = sum([x.val for x in queue])
            # update max_sum
            if curr_sum > max_sum:
                max_sum, max_level = curr_sum, curr_level
            # build next level
            queue = [y for x in queue for y in [x.left, x.right] if y]
            curr_level += 1

        return max_level


