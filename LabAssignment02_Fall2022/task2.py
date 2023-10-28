def Merge(A, B):
    new_arr = [0] * (len(A) + len(B))
    i = 0
    j = 0
    k = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            new_arr[k] = A[i]
            i += 1
        else:
            new_arr[k] = B[j]
            j += 1
        k += 1

    while i < len(A):
        new_arr[k] = A[i]
        i += 1
        k += 1

    while j < len(B):
        new_arr[k] = B[j]
        j += 1
        k += 1
    return new_arr


def Merge_Sort(A):
    i = 0
    n = len(A)
    mid_idx = (n + i) // 2
    # print(i, n)
    if n == 1:
        return A
    else:
        # print(A[i:mid_idx])
        X1 = Merge_Sort(A[:mid_idx])
        X2 = Merge_Sort(A[mid_idx:])
        X = Merge(X1, X2)
        return X


file = open("input2.txt", "r")
file_w = open('output2.txt', 'w')
size = int(file.readline())
arr = file.readline().strip().split()
arr = [int(i) for i in arr]
sorted_arr = Merge_Sort(arr)
# print(sorted_arr)
for k in range(size):
    file_w.write(str(sorted_arr[k]) + " ")
    k += 1
file.close()
file_w.close()
