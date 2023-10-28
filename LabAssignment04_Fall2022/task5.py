file = open("input5_1.txt", "r")
file_w = open("output5_1.txt", "w")
N, M, D = map(int, file.readline().split(" "))
# print(N, M, D)
new_lst = []
for i in range(M):
    new_lst_2 = list(map(int, file.readline().split(" ")))
    new_lst.append(new_lst_2)
# print(new_lst)
d = dict()
for j in range(1, N + 1):
    d[j] = []
# print(d)
for k in range(M):
    d[new_lst[k][0]].append(new_lst[k][1])
# print(d)


def BFS_SP(graph, start, goal):
    visited = []
    queue = [[start]]
    if start == goal:
        print("Time: 0")
        print("Shortest Path:", goal)
        ext = "Time: 0" + "\n" + "Shortest path: " + str(goal)
        file_w.write(ext)
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            adjacent = graph[node]
            for x in adjacent:
                new_lst_3 = list(path)
                new_lst_3.append(x)
                queue.append(new_lst_3)
                if x == goal:
                    print("Time:", len(new_lst_3) - 1)
                    print("Shortest path:", *new_lst_3)
                    file_w.write("Time: " + (str(len(new_lst_3) - 1)) + "\n")
                    file_w.write("Shortest Path: " + " ".join(str(y) for y in new_lst_3))
                    return
            visited.append(node)

    print("Path not available!!!")
    file_w.write("Path not available!!!")
    return


BFS_SP(d, 1, D)
