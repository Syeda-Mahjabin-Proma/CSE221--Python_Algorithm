file = open("input4.txt", "r")
file_w = open("output4.txt", "w")

a = int(file.readline())
id_lst = file.readline().strip().split()
marks_lst = file.readline().strip().split()
# print(id_lst, marks_lst)

tuple_lst = list(zip(id_lst, marks_lst))
tuple = [('5', '80'), ('7', '80'), ('2', '60'), ('3', '50')]
for i in range(a):
    for j in range(i + 1, a):
        if int(tuple_lst[i][1]) < int(tuple_lst[j][1]):
            temp = tuple_lst[i]
            tuple_lst[i] = tuple_lst[j]
            tuple_lst[j] = temp
        elif int(tuple_lst[i][1]) == int(tuple_lst[j][1]):
            if int(tuple_lst[i][0]) > int(tuple_lst[j][0]):
                temp = tuple_lst[i]
                tuple_lst[i] = tuple_lst[j]
                tuple_lst[j] = temp

for k in range(a):
    file_w.write("ID: " + str(tuple_lst[k][0]) + " Mark: " + str(tuple_lst[k][1]) + "\n")
    k += 1

print(tuple_lst)
file.close()
file_w.close()
