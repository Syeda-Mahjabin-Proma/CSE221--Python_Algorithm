# 1(b)
file = open("input1b.txt", "r")
file_w = open("output1b.txt", "w")
a = int(file.readline())
for i in range(a):
    b = file.readline().strip()
    c = b.split(" ")
    d = c[1:]

    if d[1] == "+":
        result = int(d[0]) + int(d[2])
    if d[1] == "-":
        result = int(d[0]) - int(d[2])
    if d[1] == "*":
        result = int(d[0]) * int(d[2])
    if d[1] == "/":
        result = int(d[0]) / int(d[2])
    line = 'The result of ' + d[0] + d[1] + d[2] + ' is ' + str(result) + "\n"
    file_w.write(line)
file.close()
file_w.close()
