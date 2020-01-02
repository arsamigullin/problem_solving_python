
# https://leetcode.com/problems/accounts-merge/submissions/
# Algo
# 1. Convert accounts to the adjacency-list representation
#   NOTE: vertex (key) is IN the set (value) as well
# 2. While converting, for each email store also a name of a person
# 3. Go over each key in graph and mark it as visited once visited
# 4. NOTE: when iterating the stack we add children of grpaph[node]. This will ensure we visited all the related emails
# In other words, suppose we have this adjaceny-list representation:
# 1: 1,2,3
# 2: 2,1
# 3: 3,1
# 4: 4
# starting from the 1 item and it's children we skip 1 (since we visited it) then we reach 2 and we add children of 2
# to the stack if the children have not been visited, then we visit 3 and add its children and so on
# This technique ensures that all the related email will be to visited and will be added to components

import collections
class Solution(object):
    def accountsMerge(self, accounts):
        graph = collections.defaultdict(set)
        email_to_name = {}
        for i in range(len(accounts)):
            name = accounts[i][0]
            for email in accounts[i][1:]:
                graph[accounts[i][1]].add(email)
                graph[email].add(accounts[i][1])
                email_to_name[email] = name
        seen = set()
        ans = []

        for email in graph:
            if email not in seen:
                seen.add(email)
                stack = [email]
                component = []
                while stack:
                    node = stack.pop()
                    component.append(node)
                    for ein in graph[node]: # this ensures all the emails will be visited
                        if ein not in seen:
                            seen.add(ein)
                            stack.append(ein)
                ans.append([email_to_name[email]] + sorted(component))
        return ans

if __name__ == "__main__":
    s = Solution()
    s.accountsMerge([["John","john_newyork@mail.com", "johnsmith@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])