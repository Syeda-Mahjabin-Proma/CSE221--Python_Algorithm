# 1(a)
file = open("input1a.txt", "r")
file_w = open("output1a.txt", "w")
a = file.readline()
# print(a)
for i in range(int(a)):
    b = int(file.readline())

    if b % 2 == 0:
        file_w.write(str(b) + " is even\n")
    else:
        file_w.write(str(b) + " is odd\n")
file.close()
file_w.close()
