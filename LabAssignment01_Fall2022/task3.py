def bubble_sort(array):
    count = 0
    for i in range(size):
        for j in range(size - i):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                count += 1
        if count == 0:
            break
    return array


file = open('input3.txt', 'r')
file_w = open('output3.txt', 'w')
size = int(file.readline().strip()) - 1
arr = file.readline().strip().split(" ")
bubble_sort(arr)
my_string = " ".join(arr)
file_w.write(my_string)
file.close()
file_w.close()
