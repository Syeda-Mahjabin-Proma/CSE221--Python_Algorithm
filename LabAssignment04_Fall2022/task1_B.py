file = open("input1B_1.txt", "r")
file_w = open("output1B_1.txt", "w")
row_col_number, total_edge = map(int, file.readline().split(" "))
# print(row_col_number, total_edge)
list_1 = [[] for j in range(row_col_number + 1)]
# print("lst 1:", list_1)
new_lst = []
for j in range(total_edge):
    str_temp = file.readline().strip().split()
    int_temp = [eval(i) for i in str_temp]
    # print(int_temp)
    new_lst.append(int_temp)
# print("empty", new_lst)
for j in range(len(new_lst)):
    list_1[new_lst[j][0]].append((new_lst[j][1], new_lst[j][2]))
print(list_1)
for i in range(len(list_1)):
    z = " ".join(str(items) for items in list_1[i])
    z = str(i) + " : " + z + "\n"
    file_w.write(z)
