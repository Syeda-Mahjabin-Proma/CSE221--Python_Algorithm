file = open("input4_5.txt", "r")
file_w = open("output4_5.txt", "w")
N, M = map(int, file.readline().split(" "))
# print(N, M)
new_lst = []
for i in range(M):
    new_lst_2 = list(map(int, file.readline().split(" ")))
    new_lst.append(new_lst_2)
# print(new_lst)
adj_list = dict()
for x in range(1, N + 1):
    adj_list[x] = []
# print(d)
for k in range(M):
    adj_list[new_lst[k][0]].append(new_lst[k][1])
# print(adj_list)
color = {}
parent = {}

for u in adj_list.keys():
    color[u] = "initially_white"
    parent[u] = None


# print(color)
# print(parent)

def dfs(u, color, parent):
    color[u] = "visited_once"
    for v in adj_list[u]:
        if color[v] == "initially_white":
            parent[v] = u
            cycle = dfs(v, color, parent)
            if cycle:
                return True
        elif color[v] == "visited_once" and parent[u] != v:
            return True
    color[u] = "other"
    return False


flag = False
a = "No Cycle"
for u in adj_list.keys():
    if color[u] == "initially_white":
        flag = dfs(u, color, parent)
        if flag == True:
            a = "Cycle"
            break

print(a)
file_w.write(a)

