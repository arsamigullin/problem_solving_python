import collections


class Solution:
    def numSteps(self, s: str) -> int:

        sl = collections.deque(s)
        cnt = 0
        while len(sl) > 1:
            cnt += 1
            if sl[-1] == '1':
                for i in range(len(sl) - 1, -1, -1):
                    if sl[i] == '0':
                        sl[i] = '1'
                        break
                    else:
                        sl[i] = '0'
                if sl[0] == '0':
                    sl.appendleft('1')
            else:
                sl.pop()
        return cnt

# this solution is not suitable in other languages
class Solution:
	def numSteps(self, s: str) -> int:
		ans=0
		while s!='1':
			if s[-1]=='1':
				s=bin(int(s,2)+1)[2:]
			else:
				s=s[:-1]
			ans+=1
		return ans