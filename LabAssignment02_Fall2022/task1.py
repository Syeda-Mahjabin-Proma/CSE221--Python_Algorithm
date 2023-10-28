file = open("input1.txt", "r")
file_w = open("output1.txt", "w")
n = int(file.readline())
id_lst = file.readline().strip().split()
marks_lst = file.readline().strip().split()
# print(id_lst, marks_lst)
for i in range(0, n):
    temp = marks_lst[i]
    temp_2 = id_lst[i]
    j = i - 1
    while j >= 0:
        if temp > marks_lst[j]:
            marks_lst[j + 1] = marks_lst[j]
            id_lst[j + 1] = id_lst[j]
            j = j - 1
        else:
            break
    marks_lst[j + 1] = temp
    id_lst[j + 1] = temp_2

# print(marks_lst)
# print(id_lst)
for k in range(n):
    file_w.write(id_lst[k] + " ")
    k += 1
