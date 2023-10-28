def BubbleSort(arr):
    arr_size = len(arr) - 1
    for i in range(arr_size):
        for j in range(arr_size - i):
            if int(arr[j][-1]) < int(arr[j + 1][-1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def seeDoctor():
    patient = new_lst[-1]
    new_lst.pop()
    # print("popped:", patient)
    file_w.write("popped:" + patient + "\n")


def enque(name_of_the_patient ):
    new_lst.append(name_of_the_patient )
    BubbleSort(new_lst)


def printQueue():
    # print("*****")
    for i in new_lst:
        # print(i)
        file_w.write(i + "\n")
    # print("*****")


file = open("input4.txt", "r")
file_w = open('output4.txt', 'w')
patient_list = file.readlines()
for i in range(len(patient_list)):
    patient_list[i] = patient_list[i].strip()
new_lst = []
for x in patient_list:
    if x == 'see doctor':
        seeDoctor()
    else:
        enque(x)

printQueue()
file.close()
file_w.close()