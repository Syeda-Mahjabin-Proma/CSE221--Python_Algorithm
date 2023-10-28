file = open("input5.txt", "r")
file_w = open("output5.txt", "w")
a = int(file.readline())
name_lst = []
time_lst = []
departure_lst = []
ext_lst = []
for i in range(a):
    train_lst = file.readline().strip().split(" ")
    name_lst.append(train_lst[0])
    time_lst.append(train_lst[-1])
    departure_lst.append(train_lst[-3])

for i in range(a):
    k = int(str(time_lst[i][:2]) + str(time_lst[i][-2:]))
    ext_lst.append(k)

# print("Name: ",name_lst)
# print("Time: ",time_lst)
# print("Departure: ",departure_lst)
# print("Extra List: ",ext_lst)
tuple_lst = list(zip(name_lst, departure_lst, time_lst, ext_lst))
for i in range(a):
    for j in range(i + 1, a):
        if tuple_lst[i][0] > tuple_lst[j][0]:
            temp = tuple_lst[i]
            tuple_lst[i] = tuple_lst[j]
            tuple_lst[j] = temp
# print(tuple_lst)
for i in range(a):
    for j in range(i + 1, a):
        if tuple_lst[i][0] == tuple_lst[j][0]:
            if tuple_lst[i][-1] < tuple_lst[j][-1]:
                temp = tuple_lst[i]
                tuple_lst[i] = tuple_lst[j]
                tuple_lst[j] = temp
# print(tuple_lst)

for k in range(a):
    file_w.write(tuple_lst[k][0] + " will departure for " + tuple_lst[k][1] + ' at ' + tuple_lst[k][-2] + "\n")
    k += 1
file.close()
file_w.close()
