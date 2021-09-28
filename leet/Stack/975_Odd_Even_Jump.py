from typing import List


class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:

        n = len(arr)
        next_odd = [0] * n
        stack = []
        '''
        example arr         [2,3,1,1,4]
                its indices [0,1,2,3,4]
        sorted by val,i [(1,2),(1,3),(2,0),(3,1),(4,4)]
        1 iteration
        stack = [2]
        2nd 
        2<3, 2 evicted, set next_odd[2]=3
        stack = [3]
        3rd
        stack=[3,0]
        4th
        0<1, 0 evicted set next_odd[0]=1
        stack = [3,1]
        5th
        both 3 and 1 < 4 and both evicted
        next_odd[1] = 4
        next_odd[3] = 4
        
        next_odd = [1, 4, 3, 4, 0]
        '''
        for val, i in sorted([(val, i) for i, val in enumerate(arr)]):
            while stack and stack[-1] < i:
                next_odd[stack.pop()] = i
            stack.append(i)

        print(next_odd)
        # the same way we get the next lower
        next_even = [0]*n
        stack = []
        '''
        example arr         [2,3,1,1,4]
                its indices [0,1,2,3,4]
        sorted by -val,i [(-4,4),(-3,1),(-2,0),(-1,2),(-1,3)]
        
        next_even = [2, 2, 3, 0, 0]
        '''
        for val, i in sorted([(-val, i) for i, val in enumerate(arr)]):
            while stack and stack[-1]<i:
                next_even[stack.pop()] = i
            stack.append(i)
        print(next_even)

        odd = [0]*n
        even = [0]*n
        odd[-1]=even[-1]=1
        '''
        for this array [2,3,1,1,4]
        next_odd =  [1, 4, 3, 4, 0]
        next_even = [2, 2, 3, 0, 0]
        odd         [0, 1, 0, 1, 1]
        even        [0, 0, 1, 0, 1]
        indices      0  1  2  3  4
        1 iteration
        i = 3
        next_odd[i]=4 even[4]=1 odd[3]=1
        next_even[i]=0 odd[0]=0 even[3]=0
        
        for this array [5,1,3,4,2]
        next_odd =  [0, 4, 3, 0, 0]
        next_even = [3, 0, 4, 4, 0]
        odd         [0, 1, 1, 0, 1]
        even        [0, 0, 1, 1, 1]
        indices      0  1  2  3  4
        in this example 1 can reach 2 (odd jump)
        3 reaches 4 (odd jump) and 4 reaches 2 (even jump)
        
        even and odd arrays keep track of possible jumps
        doing odd[i] = even[next_odd[i]] we learn if it is possible to reach end doing odd jump starting at ith position of the arr
        doing even[i] = odd[next_even[i]] we learn if it is possible to reach end doing even jump starting at ith position of the arr
        at i = 3, we can reach end(arr[-1] = 2) from 4 (arr[3]), so even[3] = 1
        at i =2 we can reach end doing odd jump to i = 3 (the i=3 position also can reach the end)
        '''
        for i in range(n-1)[::-1]:
            odd[i] = even[next_odd[i]]
            even[i] = odd[next_even[i]]

        return sum(odd)

if __name__ == '__main__':
    s = Solution()
    s.oddEvenJumps([3,2,1,6,0,5])
    s.oddEvenJumps([5,1,3,4,2])
    s.oddEvenJumps([2,3,1,1,4])