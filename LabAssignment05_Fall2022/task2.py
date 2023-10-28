file = open("input2.txt", "r")
file_w = open("output2.txt", "w")
lst = " "
for i in file:
    lst += i
lst = lst.split("\n")
count = 1


def Dijkstra(Graph, source):
    dist = {}
    dist[source] = 0
    pred = {}
    for v in Graph:
        if v != source:
            dist[v] = float("inf")
        pred[v] = None
    Q = [v for v in range(1, len(Graph) + 1)]
    while Q != []:
        upper_bound = {v: dist[v] for v in Q}
        u = min(upper_bound, key=upper_bound.get)
        Q.remove(u)
        for v, next in Graph[u].items():
            dist[v] = min(dist[v], dist[u] + next)
            pred[v] = u
    return dist


for i in range(int(lst[0])):
    q = [int(i) for i in lst[count].split(" ")]
    count += 1
    edge = {}
    for j in range(q[1]):
        lst1 = [int(i) for i in lst[count].split(" ")]
        edge[(lst1[0], lst1[1])] = lst1[2]
        count += 1
    node = [i for i in range(1, q[0] + 1)]
    next_node = {q: {} for q in node}
    print(next_node)
    for (p, q), next in edge.items():
        next_node[p][q] = next
        next_node[q][p] = next
    n = Dijkstra(next_node, 1)
    file_w.write('{}\n'.format(str(n[node[-1]])))
