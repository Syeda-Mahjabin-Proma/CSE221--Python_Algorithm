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


def findK(arr, k):
    a = []
    for i in range(0, len(arr)):
        if i == k:
            file_w.write(str(arr[k])+ "\n")

    print(a)

file = open("input3(ii).txt", "r")
file_w = open('output3(ii).txt', 'w')
file.close()
file_w.close()