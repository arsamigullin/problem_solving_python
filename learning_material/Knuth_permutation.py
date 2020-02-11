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
            #return False
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
    arr = [1,2,3]
    while s.permute(arr):
        print(arr)
