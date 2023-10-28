file = open("task3_input.txt", "r")
file_w = open("task3_output.txt", "w")
a = int(file.readline())
arr = file.readline().strip().split(" ")
arr = [eval(i) for i in arr]
name = file.readline()
arr.sort()
temp = []
work_seq = []
jack_wh = 0
jill_wh = 0
start = 0
for i in name:
    if i == "J":
        temp.append(arr[start])
        work_seq.append(arr[start])
        jack_wh += arr[start]
        start += 1
    elif i == "j":
        count = temp.pop()
        work_seq.append(count)
        jill_wh += count

print(*work_seq, sep="")
print("Jack worked for:", jack_wh)
print("Jill worked for:", jill_wh)
for i in work_seq:
    file_w.write(str(i))
file_w.write("\nJack will work for " + str(jack_wh) + " hours"
                                                      "\nJill will work for " + str(jill_wh) + " hours")
