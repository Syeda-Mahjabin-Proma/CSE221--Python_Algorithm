file = open("input1A_2.txt", "r")
file_w = open("output1A_2.txt", "w")
row_col_number, total_edge = map(int, file.readline().split(" "))
# print(row_col_number, total_edge)
mat = [[0 for i in range(0, row_col_number + 1)] for j in range(0, row_col_number + 1)]
# print("Matrix: ", mat)
for i in range(total_edge):
    str_temp = file.readline().strip().split()
    int_temp = [eval(i) for i in str_temp]
    # print(int_temp)
    mat[int_temp[0]][int_temp[1]] = int_temp[-1]
    # print("**",mat)

for j in range(len(mat)):
    z = " ".join(str(k) for k in mat[j])
    z = z + "\n"
    file_w.write(z)
