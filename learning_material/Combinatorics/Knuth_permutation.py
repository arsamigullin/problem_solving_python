# this is permutation n of n

'''
Accordint to Steven Khalim
1. The total count of permutations of an array with unique elements is math.factorial(len(arr))
2. If elements not unique the formula is
    n! / (n1! * n2! ... ni!)
    where ni is count of unique elements
'''

class KnuthPermutation:
    def permute(self, arr):
        if not arr:
            return  False
        # from the end we search the first number in decreasing order
        i = len(arr) - 2
        while i >=0 and arr[i]>arr[i+1]:
            i-=1

        if i < 0:
            arr.reverse()
            return False
        # from the end we search the first num that is greater than num[i]
        j = len(arr) - 1
        while j > i and arr[j]<arr[i]:
            j-=1

        arr[i], arr[j] = arr[j], arr[i]
        # reverse the items between i and len(arr)
        start = i + 1
        end = len(arr) - 1
        while start<end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1

        return True




if __name__ == "__main__":
    s = KnuthPermutation()
    #s.permute([4, 9, 5, 3, 1])
    import math
    arr = [0,1,2,3,4,5,6,7]
    #arr = [-6,184,10]
    #arr = [1,9,4,6,7]
    arr = [1,2,3,4]
    #s.permute(arr)
    n = math.factorial(len(arr))
    res = []
    for i in range(n):
        s.permute(arr)
        res.append(arr[:])
        print(arr)
    res.sort()
    print(res)
    # [1, 2, 3]
    # [1, 3, 2]
    # [2, 1, 3]
    # [2, 3, 1]
    # [3, 1, 2]
    # [3, 2, 1]