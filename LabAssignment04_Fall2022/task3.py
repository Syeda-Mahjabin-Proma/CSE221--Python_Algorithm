file = open("input3_1.txt", "r")
file_w = open("output3_1.txt", "w")
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
visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        # print(node, end=" ")
        file_w.write(str(node) + " ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


dfs(visited, d, 1)

