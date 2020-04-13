import collections
import typing
List = typing.List
# this problem
# https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    '''
    this is input
    we need to group the output by content, i.e. the data between (...)
    ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    '''
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for p in paths:
            splited = p.split()
            root = splited[0]
            for i in range(1, len(splited)):
                ind = splited[i].find('(')
                txt = splited[i][ind:]
                d[hash(txt)].append(root + '/' + splited[i][:ind])
        print(d)
        # this will take only duplicates
        return [val for val in d.values() if len(val) > 1]
# follow up questions
# Follow-up beyond contest:
# Imagine you are given a real file system, how will you search files? DFS or BFS?
# If the file content is very large (GB level), how will you modify your solution?
# If you can only read the file by 1kb each time, how will you modify your solution?
# What is the time complexity of your modified solution? What is the most time-consuming part and memory consuming part of it? How to optimize?
# How to make sure the duplicated files you find are not false positive?