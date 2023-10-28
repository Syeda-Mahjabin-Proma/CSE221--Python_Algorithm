file = open("input2_1.txt", "r")
file_w = open("output2_1.txt", "w")
N, M = map(int, file.readline().split(" "))
# print(N, M)
new_lst = []
for i in range(M):
    new_lst_2 = list(map(int, file.readline().split(" ")))
    new_lst.append(new_lst_2)
# print(new_lst)
d = dict()
for x in range(1, N + 1):
    d[x] = []
# print(d)
for k in range(M):
    d[new_lst[k][0]].append(new_lst[k][1])
# print(d)
visited = []
queue = []
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        # print(m, end=" ")
        file_w.write(str(m) + " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited, d, 1)
