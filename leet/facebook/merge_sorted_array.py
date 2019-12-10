def solution(nums1, m, nums2, n):
    j = 0
    for i in range(len(nums2)):
        temp = 0
        while j < len(nums1):
            if nums2[i] < nums1[j]:
                temp, nums1[j] = nums1[j], nums2[i]
                t_j = j + 1
                while t_j <len(nums1):
                    if temp < nums1[t_j]:
                        nums1[t_j], temp = temp, nums1[t_j]
                    elif t_j > m - 1:
                        nums1[t_j] = temp
                        m+=1
                        break
                    t_j+=1
                break
            elif j > m - 1:
                nums1[j] = nums2[i]
                m+=1
                break
            j+=1
    return

if __name__ == "__main__":
    solution([1,2,3,0,0,0],3 ,[2,5,6], 3)