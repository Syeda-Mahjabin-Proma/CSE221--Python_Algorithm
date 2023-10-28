file = open("input3.txt", "r")
file_w = open("output3.txt", "w")
lst = " "
for i in file:
    lst += i
lst1 = lst.split("\n")
count = 1


def Dijkstra(graph, source):
    dist = {}
    dist[source] = 0
    visited = {}
    prev = {}
    for v in graph:
        if v != source:
            dist[v] = float('inf')
        prev[v] = None
        visited[v] = 0
    Q = [v for v in range(1, len(graph) + 1)]
    while Q != []:
        upper_bound = {v: dist[v] for v in Q}
        u = min(upper_bound, key=upper_bound.get)
        Q.remove(u)
        for v, next in graph[u].items():
            dist[v] = min(dist[v], dist[u] + next)
            prev[v] = u

    return prev


def sequence(dic):
    k = []
    val = []
    for i, j in dic.items():
        k.append(i)
        val.append(j)
    if val[0] is None:
        return [k[0]]
    count = [list(dic.keys())[0]]
    count.append(dic[count[-1]])
    for i in range(len(dic)):
        if count[-1] == list(dic.keys())[-1]:
            break
        else:
            c = k.index(count[-1])
            count.append(val[c])

    return count


for i in range(int(lst1[0])):
    v = [int(i) for i in lst1[count].split(" ")]
    count += 1
    edge = {}
    for j in range(v[1]):
        lst2 = [int(i) for i in lst1[count].split(" ")]
        edge[(lst2[0], lst2[1])] = lst2[2]
        count += 1

    node = [i for i in range(1, v[0] + 1)]
    next_node = {v: {} for v in node}

    for (p, q), next in edge.items():
        next_node[p][q] = next
        next_node[q][p] = next

    path = Dijkstra(next_node, 1)
    lst = sequence(path)
    file_w.write(' '.join(str(elem) for elem in lst)+'\n')


    