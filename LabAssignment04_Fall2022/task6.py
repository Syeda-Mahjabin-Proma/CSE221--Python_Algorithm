file = open("input6_1.txt", "r")
file_w = open("output6_1.txt", "w")
N, M = map(int, file.readline().split(" "))
lst_1 = []
for i in range(N):
    read = file.readline().strip()
    x = [i for i in read]
    # print(x)
    lst_1.append(x)
print(lst_1)
number_of_dimond = 0
keyword = 'D'
for lst in lst_1:
    if keyword in lst:
        number_of_dimond += 1
print(number_of_dimond)
file_w.write(str(number_of_dimond))