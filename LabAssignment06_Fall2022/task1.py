file = open("task1_input.txt", "r")
file_w = open("task1_output.txt", "w")
a = int(file.readline())
start = []
end = []
# print(a)
for i in range(a):
    x, y = file.readline().strip().split(" ")
    start.append(x)
    end.append(y)
# print(start, end)

tuple_lst = list(zip(start, end))
for i in range(a):
    for j in range(i + 1, a):
        if int(tuple_lst[i][1]) > int(tuple_lst[j][1]):
            temp = tuple_lst[i]
            tuple_lst[i] = tuple_lst[j]
            tuple_lst[j] = temp
        elif int(tuple_lst[i][1]) == int(tuple_lst[j][1]):
            if int(tuple_lst[i][0]) > int(tuple_lst[j][0]):
                temp = tuple_lst[i]
                tuple_lst[i] = tuple_lst[j]
                tuple_lst[j] = temp
# print(tuple_lst)

main = [tuple_lst[0]]
task_count = 1
current_ft = tuple_lst[0][1]
for i in range(1, len(tuple_lst)):
    if int(tuple_lst[i][0]) >= int(current_ft):
        main.append(tuple_lst[i])
        current_ft = tuple_lst[i][1]
        task_count += 1
print(task_count)
print(main)

file_w.write(str(task_count) + "\n")
for k in range(task_count):
    file_w.write(str(main[k][0]) + " " + str(main[k][1]) + "\n")
    k += 1
