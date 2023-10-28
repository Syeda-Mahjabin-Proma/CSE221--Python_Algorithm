file = open("task2_input.txt", "r")
file_w = open("task2_output.txt", "w")
line, person = map(int, file.readline().strip().split(" "))
start = []
end = []
# print(a)
for i in range(int(line)):
    x, y = file.readline().strip().split(" ")
    start.append(x)
    end.append(y)
# print(start, end)

tuple_lst = list(zip(start, end))
for i in range(line):
    for j in range(i + 1, line):
        if (tuple_lst[i][1]) > (tuple_lst[j][1]):
            temp = tuple_lst[i]
            tuple_lst[i] = tuple_lst[j]
            tuple_lst[j] = temp
        elif (tuple_lst[i][1]) == (tuple_lst[j][1]):
            if (tuple_lst[i][0]) > (tuple_lst[j][0]):
                temp = tuple_lst[i]
                tuple_lst[i] = tuple_lst[j]
                tuple_lst[j] = temp
# print(tuple_lst)
f = []
for k in range(person):
    f.append([])
# print(f)
task_count = 0
for z in range(len(f)):
    main = [tuple_lst[0]]
    task_count += 1
    current_ft = tuple_lst[0][1]
    for x in range(1, len(tuple_lst)):
        if (tuple_lst[x][0]) >= current_ft:
            main.append(tuple_lst[x])
            current_ft = tuple_lst[x][1]
            task_count += 1
    f[z].append(main)
    for y in main:
        tuple_lst.remove(y)


print(f)
print(task_count)
file_w.write(str(task_count))
