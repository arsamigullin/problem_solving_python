import collections
from typing import List


class Solution3:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        parent = {}
        def find(p):
            parent.setdefault(p, p)
            rootP = p
            while rootP != parent[rootP]:
                rootP = parent[rootP]
            while p != rootP:
                newp = parent[p]
                parent[p] = rootP
                p = newp
            return rootP

        def union(p, q):
            rootP = find(p)
            rootQ = find(q)
            if rootP == rootQ:
                return
            parent[rootQ] = rootP

        email_to_name = {}

        # here we create a component based on the emails of the current account
        # NOTE: after this loop the emails from the same component can have different parents
        # because of nature of Union-Find
        for account in accounts:
            for email in account[1:]:
                email_to_name[email] = account[0]
                union(email, account[1])

        res = collections.defaultdict(list)
        # in this loop we find the parent based on the find mehtod
        # which will flatten the tree and assign the only parent for the current email
        for email in email_to_name:
            par = find(email)
            res[par].append(email)

        return [[email_to_name[name]] + sorted(emails) for name, emails in res.items()]


class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            parent.setdefault(x, x)
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        email_to_id = {}
        email_to_name = {}
        i = 0
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                email_to_name[email] = name
                if email not in email_to_id:
                    email_to_id[email] = i
                    i += 1
                union(email_to_id[email], email_to_id[account[1]])

        res = collections.defaultdict(list)

        for email in email_to_name:
            res[find(email_to_id[email])].append(email)

        return [[email_to_name[v[0]]] + sorted(v) for v in res.values()]



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
class Solution1(object):
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
    s = Solution1()
    s.accountsMerge(
        [["John", "john_newyork@mail.com", "johnsmith@mail.com", "johnsbarabun@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
         ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
    s.accountsMerge([["John","john_newyork@mail.com", "johnsmith@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])