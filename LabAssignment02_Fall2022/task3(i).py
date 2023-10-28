def Partition(A, pivot, lst_idx):
    i = pivot + 1
    j = i
    while j <= lst_idx:
        if A[j] < A[pivot]:
            A[i], A[j] = A[j], A[i]
            i += 1
        j = j + 1
    A[pivot], A[i - 1] = A[i - 1], A[pivot]
    # print(A, pivot, lst_idx, i)
    return (i - 1)


def Quick_Sort(A, p, r):
    # print(p, r)
    if p >= r:
        return 1
    else:
        q = Partition(A, p, r)
        # print(p, q, r)
        Quick_Sort(A, q + 1, r)
        Quick_Sort(A, p, q - 1)


# arr = [5, -1, 10, 2, 8]
# n = len(arr)
# Quick_Sort(arr, 0, n - 1)
# print(arr)
file = open("input3(i).txt", "r")
file_w = open('output3(i).txt', 'w')
size = int(file.readline())
arr = file.readline().strip().split()
arr = [int(i) for i in arr]
Quick_Sort(arr, 0, size-1)
# print(sorted_arr)
for k in range(size):
    file_w.write(str(arr[k]) + " ")
    k += 1
file.close()
file_w.close()
