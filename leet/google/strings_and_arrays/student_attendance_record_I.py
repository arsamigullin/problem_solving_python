# this problem
# https://leetcode.com/problems/student-attendance-record-i/
import re
class Solution:
    def checkRecord(self, s: str) -> bool:
        cntA = 0
        cntL = 0
        for letter in s:
            if letter == 'A':
                cntA+=1
            elif letter == 'L':
                cntL+=1
            if letter!='L':
                cntL=0
            if cntA>1:
                return False
            if cntL>2:
                return False
        return True

    def checkRecord2(self, s: str) -> bool:
        return s.count('A')<=1 and s.find('LLL') == -1

    def checkRecord2(self, s: str) -> bool:
        return 

                