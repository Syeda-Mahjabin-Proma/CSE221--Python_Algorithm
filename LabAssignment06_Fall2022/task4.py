import math

file = open("task4_input.txt", "r")
file_w = open("task4_output.txt", "w")
x = len(file.readlines())
# print('Total lines:', x)
file.close()
file = open("task4_input.txt", "r")
for i in range(x):
    a, b = map(int, file.readline().strip().split(" "))
    if a == 0 and b == 0:
        break
    else:
        lst_1 = []
        for j in range(a, b + 1):
            lst_1.append(j)
            count = 0
            for k in lst_1:
                one_dec = str(round(math.sqrt(k), 1))
                if one_dec[-1] == "0":
                    count += 1

        # print("list 1:", lst_1)
        print(count)
        file_w.write(str(count) + "\n")
